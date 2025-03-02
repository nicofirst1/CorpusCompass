"""
The module contains classes used for the CorpusCompass model
"""

from PySide6.QtCore import QObject, Signal
from typing import List, Dict, Tuple
import pandas as pd
from src.model.variables_speakers import Variable, VariableValue, Speaker
from src.model.files import File, FileLoader
from src.model.variables_speaker_detection import (
    SpeakerDetector,
    AnnotationDetector,
    SpeakerFormats,
)
from src.model.dataset_creation import DatasetCreator
from src.utils.DCThread import DCThread, CustomThread, generate_dataset
import src.utils.file_utils as file_utils
import json
import os
import ast


class CorpusCompassModel:
    """
    Main-Class for managing the corpus-compass model. Provides methods for
    creating, modifying and saving of a project.
    """

    def __init__(self) -> None:
        self.current_project: Project = None

    def is_project_loaded(self) -> bool:
        """Check, if there is a project currently loaded in.

        Returns:
            bool: If a project is loaded in, return True, otherwise return False
        """
        if not self.current_project:
            return False
        return True

    def create_new_project(
        self, proj_name: str, proj_description: str = "", proj_dir: str = None
    ) -> None:
        """Creates a new project with the given name and description.

        Args:
            proj_name (str): The name of the project.
            proj_description (str, optional): The description of the project. Defaults to "".
            proj_dir (str, optional): The directory, where the project should be saved. Defaults to None.
        """
        self.current_project = Project(proj_name, proj_description, proj_dir)

    def import_project(self, project_path: str) -> None:
        """Imports a project from a given path. The project is loaded in and set as the current project.
        The path must lead to a directory, that contains a project_metadata.json file.

        Args:
            project_path (str): The path to the project directory.
        """
        self.current_project = Project.load_project(project_path)

    def save_project(self, project_path: str) -> None:
        """Saves the current project to a given path.

        Args:
            project_path (str): The path, where the project should be saved.
        """
        if self.current_project:
            self.current_project.save_project(project_path)

    def close_project(self) -> None:
        """Closes the current project by stopping running threads"""
        if self.current_project:
            self.current_project.close()
        self.current_project = None


class Project(QObject):
    """Class contains all information about a project, like:
        - Speakers, dependent and independent variables
        - Corpora files with their content
        - Position of speakers and annotations in the corpora

    Args:
        QObject (_type_): Inherits from QObject, in order to send signals to the
                          controller.
    """

    # Create  signals that are used for sending updates to the gui
    error_occurred_signal = Signal(str)  # Is sent if the model throws an exception
    file_added_signal = Signal(File)  # Is sent if a new file has been loaded
    file_removed_signal = Signal(File)  # Is sent if a file has been removed
    iv_changed_signal = Signal(dict)  # Is sent if the IV's have been modified
    speaker_changed_signal = Signal(
        dict
    )  # Is sent if the Speaker data have been modified
    dv_changed_signal = Signal(dict)  # Is sent if the DV's have been modified
    dv_values_changed_signal = Signal(
        dict
    )  # Is sent if the DV-values have been modified
    annotation_formats_changed_signal = Signal(
        dict
    )  # Is sent if the annotation formats have been modified
    speaker_preview_signal = Signal(
        dict
    )  # Is sent if a preview of the detected speakers was created
    annotation_preview_signal = Signal(
        pd.DataFrame
    )  # Is sent if a preview of the detected annotations was created
    corpus_analysis_data_signal = Signal(
        dict
    )  # Is sent if the analysis of the corpus is finished

    def __init__(
        self, proj_name: str, proj_description: str = "", proj_dir: str = None
    ) -> None:
        """Creates a new project for the analysis of a corpus.

        Args:
            proj_name (str): The name of the project.
            proj_description (str, optional): What the project is about. Defaults to "".
            proj_dir (str, optional): Where the project files are located. Defaults to None.
        """
        super().__init__()
        self.proj_name: str = proj_name
        self.proj_description: str = proj_description
        if proj_dir:
            self.proj_directory = os.path.join(proj_dir, proj_name)
        else:
            self.proj_directory = None

        # files contains all corpora that are loaded in. File_loader will contain
        # an instance of the FileLoader class, when there are files to load in.
        self.file_loader: FileLoader = None
        self.files: List[File] = []

        # The following four dictionaries/list contain the names and data for dependent-
        # and independent variables, dependent variable values and speakers.
        self.independent_variables: Dict[str, Variable] = {}
        self.dependent_variables: Dict[str, Variable] = {}
        self.dependent_variable_values: List[VariableValue] = []
        self.speakers: Dict[str, Speaker] = {}

        # The speaker detector can detect, what text passage is spoken by a speaker
        # The data is then saved in the dataframe "speakers_in_files"
        self.speaker_detector: SpeakerDetector = SpeakerDetector()
        self.speakers_in_files: pd.DataFrame = pd.DataFrame(
            columns=[
                "speaker_name",
                "speaker_start",
                "speaker_end",
                "spoken_text_start",
                "spoken_text_end",
                "file_name",
                "file_version",
            ]
        )

        # Contains a list of symbols, that the user can use to define a annotation
        # format
        self.annotation_symbols: List[str] = [
            "$",
            "[",
            "]",
            "{",
            "}",
            "%",
            "&",
            "(",
            ")",
            ".",
            "_",
        ]

        # The annotation detector can detect annotations, if a correct annotation
        # format is passed to him. The found annotations are stored in the
        # dataframe "annotations_in_files"
        self.annotation_detector: AnnotationDetector = AnnotationDetector()
        self.annotations_in_files: pd.DataFrame = pd.DataFrame(
            columns=[
                "token",
                "identifier",
                "annotation_start",
                "annotation_end",
                "annotation_string",
                "file_name",
                "file_version",
            ]
        )

        # The dataset creator creates datasets from the corpora files, that can be
        # used for further analysis
        self.dataset_creator: DatasetCreator = DatasetCreator(self)

        # Section for threads

        self.annotation_preview_thread: CustomThread = None
        self.speaker_preview_thread: CustomThread = None
        self.dc_thread: DCThread = None
        # List to hold the references to the worker threads. Once a worker thread
        # is finished, it is removed from the list.
        self.worker_threads: List[CustomThread] = []

        # Create the project in files if wanted by the user
        if proj_dir:
            if not os.path.exists(self.proj_directory):
                os.makedirs(self.proj_directory)

    def close(self) -> None:
        """Closes the current project"""
        if self.speaker_preview_thread and self.speaker_preview_thread.isRunning():
            self.speaker_preview_thread.terminate()
        if (
            self.annotation_preview_thread
            and self.annotation_preview_thread.isRunning()
        ):
            self.annotation_preview_thread.terminate()
        self.remove_all_worker_threads()

    def get_name(self) -> str:
        """Returns the name of the project.

        Returns:
            str: The name of the project.
        """
        return self.proj_name

    def get_description(self) -> str:
        """Returns the description of the project.

        Returns:
            str: The description of the project.
        """
        return self.proj_description

    def add_iv(self, iv_name: str, iv_values: List[str] = None) -> None:
        """Creates a new independent variable (iv) and adds it to the project.
        If an iv with the same name already exists, the creation of the new iv
        will fail.

        Args:
            iv_name (str): The name of the iv. Each iv must have a unique name.
            iv_values (List[str], optional): A list of iv-values, that will automatically be assigned
                                             to the newly created iv-object. Defaults to None.
        """
        # Check, if an iv with the same name already exists
        if iv_name in self.independent_variables:
            self.error_occurred_signal.emit(
                f'The Independent Variable with the name "{iv_name}" does already exist!'
            )
            return

        # Create the iv
        self.independent_variables[iv_name] = Variable(iv_name, iv_values)

    def remove_iv(self, iv_name: str) -> None:
        """Removes an independent variable (iv) from the project. Also removes
        all iv-values and references from Speakers to the iv-values. Will fail,
        if no iv with the given name was found.

        Args:
            iv_name (str): The name of the iv, that should be deleted
        """
        # Check, if the iv exists
        if iv_name not in self.independent_variables:
            self.error_occurred_signal.emit(
                f'The Independent Variable with the name "{iv_name}" was not found!'
            )
            return

        # Get the iv and delete all it's iv-values first
        iv = self.independent_variables[iv_name]
        for iv_value in iv.get_variable_values().copy():
            iv.remove_variable_value(iv_value)

        # Delete the iv itself
        del self.independent_variables[iv_name]

    def exists_iv_value(self, iv_value: str) -> bool:
        """Checks, if a independent variable value already exists in the project.

        Args:
            iv_value (str): The name of the independent variable value, that should be checked.

        Returns:
            bool: True, if the independent variable value already exists, else False.
        """
        for iv in self.independent_variables.values():
            if iv.has_variable_value(iv_value):
                return True
        return False

    def get_iv(self, iv_name: str) -> Variable:
        """Returns a independent variable with the given name. If no independent variable with the
        given name was found, the method returns None.

        Args:
            iv_name (str): The name of the independent variable, that should be returned.

        Returns:
            Variable: The independent variable with the given name. If no independent variable was found, return None.
        """
        if iv_name in self.independent_variables:
            return self.independent_variables[iv_name]
        return None

    def get_iv_value(self, iv_value_name: str) -> VariableValue:
        """Returns a independent variable value with the given name. If no independent variable value with the
        given name was found, the method returns None.

        Args:
            iv_value (str): The name of the independent variable value, that should be returned.

        Returns:
            VariableValue: The independent variable value with the given name. If no independent variable value was found, return None.
        """
        for iv in self.independent_variables.values():
            if iv.has_variable_value(iv_value_name):
                return iv.get_variable_value(iv_value_name)
        return None

    def exists_iv(self, iv_name: str) -> bool:
        """Checks, if a independent variable already exists in the project.

        Args:
            iv_name (str): The name of the independent variable, that should be checked.

        Returns:
            bool: True, if the independent variable already exists, else False.
        """
        return iv_name in self.independent_variables

    def add_iv_value_to_iv(self, iv_name: str, iv_value_name: str) -> None:
        """Adds a independent variable value to an independent variable (iv).
        Fails, if no iv with the given name was found, or if the iv-value already exists.

        Args:
            iv_name (str): The name of the iv, to which a new value should be added.
            iv_value_name (str): The new iv-value, that should be added.
        """
        # Check, if the iv exists
        if iv_name not in self.independent_variables:
            self.error_occurred_signal.emit(
                f'The Independent Variable with the name "{iv_name}" was not found!'
            )
            return

        # Check, if the iv-value already exists. If not, add the new iv-value to the iv.
        iv = self.independent_variables[iv_name]
        success = iv.add_variable_value(iv_value_name)

        if not success:
            self.error_occurred_signal.emit(
                f'The Independent Variable "{iv_name}" already contains a variable value called "{iv_value_name}"!'
            )

    def remove_iv_value_from_iv(self, iv_name: str, iv_value_name: str) -> None:
        """Removes a independent variable value from an independent variable (iv).
        Also removes references from speakers to this iv-value.
        Fails, if no iv with the given name was found, or if the iv-value doesn't exist.

        Args:
            iv_name (str): The name of the iv, from which the value should be removed.
            iv_value_name (str): The name of iv-value, that should be removed.
        """
        # Check, if the iv exists
        if iv_name not in self.independent_variables:
            self.error_occurred_signal.emit(
                f'The Independent Variable with the name "{iv_name}" was not found!'
            )
            return

        iv = self.independent_variables[iv_name]
        iv_value = iv.get_variable_value(iv_value_name)

        # Check, if the iv-value exists.
        if not iv_value:
            self.error_occurred_signal.emit(
                f'The Independent Variable "{iv_name}" does not contain a variable value called "{iv_value_name}"!'
            )
            return

        # Remove the iv-value.
        iv.remove_variable_value(iv_value_name)

    def get_parent_name_of_iv_value(self, iv_value_name: str) -> str:
        """Returns the name of the independent variable, that contains the iv-value.

        Args:
            iv_value_name (str): The name of the iv-value, that should be checked.

        Returns:
            str: The name of the independent variable, that contains the iv-value.
        """
        iv_value = self.get_iv_value(iv_value_name)
        if iv_value:
            return iv_value.get_parent().get_name()
        return None

    def get_iv_values_from_speaker(self, speaker_name: str) -> List[str]:
        """Returns a list of iv-values, that are assigned to a speaker. If no speaker
        with the given name was found, the method returns an empty list.

        Args:
            speaker_name (str): The name of the speaker, that should be checked.

        Returns:
            List[str]: A list of iv-values, that are assigned to the speaker.
        """
        if speaker_name in self.speakers:
            return [
                iv_value.name
                for iv_value in self.speakers[speaker_name].get_iv_values()
            ]
        return []

    def get_iv_printable(self) -> Dict[str, List[str]]:
        """Returns the independent variables in a more readable/printable way.
        An example output could be:
        { "Age": ["Young", "Old"], "Language": ["German", "English"]}

        Returns:
            Dict[str, List[str]]: A dictionary, where the key represents the iv-
                                  name and the value is a list containing the iv-values.
        """
        res = {}
        for iv_name, iv in self.independent_variables.items():
            res[iv_name] = [iv_value.name for iv_value in iv.get_variable_values()]
        return res

    def update_iv_from_frontend(self, data: dict) -> None:
        """Updates the independent variables from the frontend. The data is a dictionary,
        that contains the independent variables and their iv-values.

        Example data:
        {
            "Age": ["Young", "Old"],
            "Language": ["German", "English"]
        }

        Args:
            data (dict): The data, that contains the independent variables and their iv-values.
        """
        # Delete all ivs
        for iv in list(self.independent_variables.keys()):
            self.remove_iv(iv)

        # Add the ivs from the data
        for iv_name, iv_values in data.items():
            self.add_iv(iv_name, iv_values)

        # Emit the signal for the frontend, that the ivs have changed
        self.iv_changed_signal.emit(self.get_iv_printable())
        self.speaker_changed_signal.emit(self.get_speakers_printable())

    def save_iv_as_json(self, filepath: str) -> None:
        """Stores the independent variables as a json file under the provided path.

        Args:
            filepath (str): The file path, where the file is supposed to be stored.
        """
        iv_dict = Variable.to_dict(self.independent_variables.values())

        with open(filepath, "w") as outfile:
            json.dump(iv_dict, outfile, indent=4)

    def exists_speaker(self, speaker_name: str) -> bool:
        """Checks, if a speaker with the same name already exists

        Args:
            speaker_name (str): The name, that should be checked

        Returns:
            bool: True, if the speaker name is already stored in the project, else False
        """
        return speaker_name in self.speakers

    def get_speaker(self, speaker_name: str) -> Speaker:
        """Returns a speaker with the given name. If no speaker with the given name was found,
        the method returns None.

        Args:
            speaker_name (str): The name of the speaker, that should be returned.

        Returns:
            Speaker: The speaker with the given name. If no speaker was found, return None.
        """
        if self.exists_speaker(speaker_name):
            return self.speakers[speaker_name]
        return None

    def add_speaker(
        self, speaker_name: str, iv_values: List[str] = None, color: str = None
    ) -> None:
        """Adds a new speaker to the project. Fails, if a speaker with the same name already exists.

        Args:
            speaker_name (str): The name of the speaker, that should be added.
            iv_values (List[str], optional): Independent variable values that should be
                                                       assigned to the speaker. Defaults to None.
        """
        # Check, if a speaker with the same name already exists
        if self.exists_speaker(speaker_name):
            self.error_occurred_signal.emit(
                f'The Speaker with the name "{speaker_name}" does already exist!'
            )
            return

        iv_values_temp = []

        # Check, if the iv-values exist
        if iv_values:
            for iv_value_name in iv_values:
                if not self.exists_iv_value(iv_value_name):
                    self.error_occurred_signal.emit(
                        f'The Independent Variable Value "{iv_value_name}" does not exist!'
                    )
                    return
                iv_values_temp.append(self.get_iv_value(iv_value_name))

        # Create the Speaker
        self.speakers[speaker_name] = Speaker(
            name=speaker_name, iv_values=iv_values_temp, color=color
        )

    def remove_speaker(self, speaker_name: str) -> None:
        """Removes a speaker from the project. Also removes all references from the iv-values to the speaker.

        Args:
            speaker_name (str): The name of the speaker, that should be removed.
        """

        # Check, if the speaker exists
        if speaker_name not in self.speakers:
            self.error_occurred_signal.emit(
                f'The Speaker with the name "{speaker_name}" was not found!'
            )
            return

        # Get the iv and delete the reference from his iv-values to him
        speaker = self.speakers[speaker_name]
        for iv_value in speaker.get_iv_values().copy():
            iv_value.remove_speaker(speaker)

        # Delete the speaker
        del self.speakers[speaker_name]

    def assign_iv_value_to_speaker(
        self, speaker_name: str, iv_name: str, iv_value_name: str
    ) -> None:
        """Assigns a iv-value to a speaker. Fails, if the iv, the speaker or the iv-value doesn't exist.

        Args:
            speaker_name (str): The name of the speaker, that should be assigned the iv-value.
            iv_name (str): The name of the iv, that contains the iv-value.
            iv_value_name (str): The name of the iv-value, that should be assigned.
        """
        # Check, if the iv exists
        if iv_name not in self.independent_variables:
            self.error_occurred_signal.emit(
                f'The Independent Variable with the name "{iv_name}" was not found!'
            )
            return

        iv = self.independent_variables[iv_name]

        # Check, if the speaker exists
        if speaker_name not in self.speakers:
            self.error_occurred_signal.emit(
                f'The Speaker with the name "{speaker_name}" was not found!'
            )
            return

        speaker = self.speakers[speaker_name]

        # Check, if the iv-value exists
        if not iv.has_variable_value(iv_value_name):
            self.error_occurred_signal.emit(
                f'The Independent Variable "{iv_name}"  does not contain a variable value called "{iv_value_name}"!'
            )
            return

        iv_value = iv.get_variable_value(iv_value_name)

        # Assign the iv-value to the speaker
        speaker.add_iv_value(iv_value)

    def remove_iv_value_from_speaker(
        self, speaker_name: str, iv_name: str, iv_value_name: str
    ) -> None:
        """Removes a iv-value from a speaker. Fails, if the iv, the speaker or the iv-value doesn't exist.

        Args:
            speaker_name (str): The name of the speaker, from which the iv-value should be removed.
            iv_name (str): The name of the iv, that contains the iv-value.
            iv_value_name (str): The name of the iv-value, that should be removed.
        """
        # Check, if the iv exists
        if iv_name not in self.independent_variables:
            self.error_occurred_signal.emit(
                f'The Independent Variable with the name "{iv_name}" was not found!'
            )
            return

        iv = self.independent_variables[iv_name]

        # Check, if the speaker exists
        if speaker_name not in self.speakers:
            self.error_occurred_signal.emit(
                f'The Speaker with the name "{speaker_name}" was not found!'
            )
            return

        speaker = self.speakers[speaker_name]

        # Check, if the iv-value exists
        if not iv.has_variable_value(iv_value_name):
            self.error_occurred_signal.emit(
                f'The Independent Variable "{iv_name}"  does not contain a variable value called "{iv_value_name}"!'
            )
            return

        iv_value = iv.get_variable_value(iv_value_name)

        # Remove the iv-value-reference from the speaker
        speaker.remove_iv_value(iv_value)

    def get_speakers_printable(self) -> Dict[str, Tuple[Dict[str, str], str]]:
        """Returns the speakers in a more readable/printable way. An example output could be:
        { "Speaker A": ({"Age": "Old"}, "#250A25"), "Speaker B": ({"Language": "German", "Age": "Young"}, "#250A25") }

        Returns:
            Dict[str, List[Dict[str, str], str]]: A dictionary, where the key represents the speaker-
                                  name and the value is a 2D-list containing the ivs with iv-values and the colors.
        """
        res = {}
        for speaker_name, speaker in self.speakers.items():
            iv_names = {}
            color = speaker.get_color()
            res[speaker_name] = [iv_value.name for iv_value in speaker.get_iv_values()]
            for iv_value in speaker.get_iv_values():
                iv_names[iv_value.get_parent().get_name()] = iv_value.get_name()
            res[speaker_name] = (iv_names, color)
        return res

    def update_speakers_from_frontend(self, data: dict) -> None:
        """Updates the speakers from the frontend. The data is a dictionary, that contains
        the speaker-names, their iv-values and the color of the speaker. No color
        is indicated by None.

        Example data:
        {
            "Speaker A": ({"Age": "Old"}, "#250A25"),
            "Speaker B": ({"Language": "German", "Age": "Young"}, "#250A25")
        }

        Args:
            data (dict): The data, that contains the speakers, their iv-values and colors.
        """
        # Delete all speakers
        for speaker in list(self.speakers.keys()):
            self.remove_speaker(speaker)

        # Add the speakers from the data
        for speaker_name, (iv_values, color) in data.items():
            iv_value_names = list(iv_values.values())
            self.add_speaker(speaker_name, iv_value_names, color)

        # Emit the signal for the frontend, that the speakers have changed
        self.speaker_changed_signal.emit(self.get_speakers_printable())
        self.iv_changed_signal.emit(self.get_iv_printable())

    def get_speaker_format(self) -> str:
        """Returns the speaker format, that is currently used in the project.
        Currently supported formats are "STANDARD", "PRAAT", "ELAN" and "FLEX"

        Returns:
            str: The speaker format."
        """
        return self.speaker_detector.get_speaker_format_str()

    def set_speaker_format(
        self, speaker_format: SpeakerFormats | str, custom_format: str = None
    ) -> None:
        """Sets the speaker format for the project. Currently supported formats are
        "STANDARD", "PRAAT", "ELAN", "FLEX" and "CUSTOM".

        Args:
            speaker_format (str): The speaker format, that should be set.
            custom_format (str, optional): A custom speaker format, that should be set. Defaults to None.
        """
        self.speaker_detector.set_speaker_format(speaker_format, custom_format)

    def get_speaker_preview(self, speaker_format: str) -> None:
        """Creates a preview of the detected speakers for a given speaker format.
        and sends it to the frontend by sending a signal.

        Method works in a separate Thread

        Args:
            speaker_format (str): The currently selected speaker format
        """
        if self.speaker_preview_thread and self.speaker_preview_thread.isRunning():
            self.speaker_preview_thread.terminate()

        kwargs = {"speaker_format": speaker_format}
        self.speaker_preview_thread = CustomThread(
            method2run=self._get_speaker_preview,
            signal=self.speaker_preview_signal,
            **kwargs,
        )
        self.speaker_preview_thread.start()

    def _get_speaker_preview(self, speaker_format: str) -> dict:
        """Creates a preview of the detected speakers

        Args:
            speaker_format (str): The currently selected speaker format
        """
        detected_speakers = self.speaker_detector.detect_speakers(
            self.files, speaker_format=speaker_format
        )
        distinct_speakers = detected_speakers["speaker_name"].unique()
        distinct_speakers_count = len(distinct_speakers)
        data = {}
        speaker_data = {}
        for speaker in distinct_speakers:
            speaker_count = len(
                detected_speakers[detected_speakers["speaker_name"] == speaker]
            )
            speaker_data[speaker] = speaker_count
        data["Speaker_Total"] = distinct_speakers_count
        data["Speaker_Data"] = speaker_data
        return data

    def load_files(self, file_paths: List[str], is_synchronous=False) -> None:
        """Loads files into the project. The files are loaded in a separate thread.
        If the loading process is finished, the method "load_files_finished" is called.

        Args:
            file_paths (List[str]): A list of file paths, that should be loaded in.
        """
        self.file_loader = FileLoader(
            file_paths=file_paths, use_signal=not is_synchronous
        )

        if not is_synchronous:
            # Connect signals
            self.file_loader.loading_file_finished.connect(self.add_file)
            self.file_loader.finished.connect(self.load_files_finished)

            # Start loading files in a separate thread
            self.file_loader.start()
        else:
            files = self.file_loader.run()
            for file in files:
                self.add_file(file)

    def update_files(self, files: List[File], is_synchronous=False) -> None:
        """Updates the files in the project. The files are loaded in a separate thread.
        If the loading process is finished, the method "load_files_finished" is called.

        Args:
            file_paths (List[str]): A list of file paths, that should be loaded in.
        """
        if len(files) == 0:  # No files need to be updated
            return

        self.file_loader = FileLoader(
            files_to_reload=files, use_signal=not is_synchronous
        )

        if not is_synchronous:
            # Connect signals
            self.file_loader.loading_file_finished.connect(self.add_file)
            self.file_loader.finished.connect(self.load_files_finished)

            # Start loading files in a separate thread
            self.file_loader.start()
        else:
            files = self.file_loader.run()
            for file in files:
                self.add_file(file)

    def add_file(self, file: File) -> None:
        """Adds a file to the project. Sends a signal, that the file was added.

        Args:
            file (File): The file, that should be added.
        """
        self.files.append(file)
        self.file_added_signal.emit(file)

    def remove_file(self, file: File) -> None:
        """Removes a file from the project. Sends a signal, that the file was removed.

        Args:
            file (File): The file, that should be removed.
        """
        self.files.remove(file)
        # TODO: Also delete the speaker and annotation data of the file
        self.file_removed_signal.emit(file)

    def load_files_finished(self) -> None:
        """Is called, when the loading process of the files is finished."""
        self.file_loader = None

    def get_file(self, file_name: str) -> File:
        """Returns a file with the given name. If no file with the given name was found,
        the method returns None.

        Args:
            file_name (str): The name of the file, that should be returned.

        Returns:
            File: The file with the given name. If no file was found, return None.
        """
        for file in self.files:
            if file.name == file_name:
                return file

        return None

    def get_files(self) -> List[File]:
        """Returns all files, that are currently loaded in the project.

        Returns:
            List[File]: A list of all files in the project.
        """
        return self.files.copy()

    def get_filepath_from_filename(self, file_name: str) -> str:
        """Returns the file path of a file with the given name. If no file with the given name was found,
        the method returns None.

        Args:
            file_name (str): The name of the file, that should be checked.

        Returns:
            str: The file path of the file with the given name. If no file was found, return None.
        """
        for file in self.files:
            if file.name == file_name:
                return file.path

        return None

    def get_annotation_symbols(self) -> List[str]:
        """Returns the annotation symbols, that are currently used in the project.

        Returns:
            List[str]: A list of annotation symbols.
        """
        return self.annotation_symbols

    def exists_annotation_symbol(self, annotation_symbol: str) -> bool:
        """Checks, if an annotation symbol is already used in the project.

        Args:
            annotation_symbol (str): The annotation symbol, that should be checked.

        Returns:
            bool: True, if the annotation symbol is already used, else False.
        """
        return annotation_symbol in self.annotation_symbols

    def add_annotation_symbol(self, annotation_symbol: str) -> None:
        """Adds a new annotation symbol to the project. Fails, if the annotation symbol
        is already used.

        Args:
            annotation_symbol (str): The annotation symbol, that should be added.
        """
        if self.exists_annotation_symbol(annotation_symbol):
            self.error_occurred_signal.emit(
                f'The annotation symbol "{annotation_symbol}" does already exist!'
            )
            return
        self.annotation_symbols.append(annotation_symbol)

    def remove_annotation_symbol(self, annotation_symbol: str) -> None:
        """Removes an annotation symbol from the project. Fails, if the annotation symbol
        is not used in the project.

        Args:
            annotation_symbol (str): The annotation symbol, that should be removed.
        """
        if not self.exists_annotation_symbol(annotation_symbol):
            self.error_occurred_signal.emit(
                f'The annotation symbol "{annotation_symbol}" was not found and could not be removed!'
            )
            return
        self.annotation_symbols.remove(annotation_symbol)

    def detect_speakers(
        self,
        add_new_speakers: bool = True,
        is_synchronous: bool = True,
        save_detected_speakers: bool = False,
    ) -> None:
        """Detects speakers in the corpora files. The detected speakers are stored in the
        dataframe "speakers_in_files". If "add_new_speakers" is set to True, new speakers
        are automatically added to the project.

        Args:
            add_new_speakers (bool, optional): If set to True, new speakers are automatically
                                               added to the project. Defaults to True.
            is_synchronous (bool, optional): If True, the speakers are detected in a separate Thread
            save_detected_speakers (bool, optional): If the detected speakers should
                                                     be saved in the project files
        """
        if is_synchronous:
            self._detect_speakers(add_new_speakers)
        else:
            self.add_worker_thread(
                target=self._detect_speakers,
                result_signal=None,
                kwargs={
                    "add_new_speakers": add_new_speakers,
                    "save_detected_speakers": save_detected_speakers,
                },
            )

    def _detect_speakers(
        self,
        add_new_speakers: bool = True,
        send_signal: bool = True,
        save_detected_speakers: bool = False,
    ) -> None:
        """Helper method for "detect_speakers". Might be run in a separate Thread.

        Args:
            add_new_speakers (bool, optional): If detected speakers are automatically
                                               added to the project. Defaults to True.
            send_signal (bool, optional): If a signal should be send to the frontend
                                          in order to update it.
            save_detected_speakers (bool, optional): If the detected speakers should
                                                     be saved in the project files
        """
        detected_speakers = self.speaker_detector.detect_speakers(self.files)
        if save_detected_speakers:
            self.save_detected_speakers(detected_speakers)

        if detected_speakers.empty:  # If no speakers were detected, quit the method
            return
        self.speakers_in_files = detected_speakers

        if not add_new_speakers:  # If the user doesn't want to add the newly detected speakers, quit the method
            return

        # Add the newly detected speakers to the metadata
        speaker_names = detected_speakers["speaker_name"].unique()
        for speaker_name in speaker_names:
            if self.exists_speaker(speaker_name):
                continue
            self.add_speaker(speaker_name)
        if send_signal:
            self.speaker_changed_signal.emit(self.get_speakers_printable())

    def get_detected_speakers(self) -> pd.DataFrame:
        """Returns the detected speakers in the corpora files.

        Returns:
            pd.DataFrame: The detected speakers in the corpora files.
        """
        return self.speakers_in_files.copy()

    def detect_annotations(
        self,
        add_new_variable_values: bool = True,
        annotation_formats: List[str] = None,
        inplace: bool = True,
    ) -> None | pd.DataFrame:
        """Detects variable values in the corpora files. The detected variable values are stored
        in the dataframe "annotations_in_files". If "add_new_variable_values" is set to True, new
        variable values are automatically added to the project.

        Args:
            add_new_variable_values (bool, optional): If set to True, new variable values are automatically
                                                      added to the project. Defaults to True.
            annotation_formats (List[str], optional): A list of annotation formats, that should be used for the detection.
                                                        Important: Add the annotation orders to the AnnotationDetector first.
                                                        Defaults to None.
            inplace (bool, optional): If set to True, the detected variable values are stored in the project. If set to False,
                                        the detected variable values are returned. Defaults to True.

        """
        detected_dv_values = self.annotation_detector.detect_annotations(
            self.files, annotation_formats
        )
        res = None if inplace else detected_dv_values
        if detected_dv_values.empty:
            return res

        self.annotations_in_files = detected_dv_values

        if not add_new_variable_values:
            return res

        # Add the newly detected dvs to the metadata
        variable_values = detected_dv_values["identifier"].explode().unique()

        for variable_value in variable_values:
            if self.exists_dv_value(variable_value):
                continue
            self.add_dv_value(variable_value)

        return res

    def get_detected_annotations(self) -> pd.DataFrame:
        """Returns the detected variable values in the corpora files.

        Returns:
            pd.DataFrame: The detected variable values in the corpora files.
        """
        return self.annotations_in_files.copy()

    def get_annotation_preview(
        self, annotation_format: str, is_synchronous: bool = False
    ) -> None | pd.DataFrame:
        """Detects for a given annotation format the annotations in the corpora files.
        This is done in a asynchronous way, the results are sent to the frontend using
        the signal "annotation_preview_signal".
        """
        annotation_re = self.annotation_detector.get_regex_from_annotation_format(
            annotation_format, "token", "identifier"
        )
        max_amount_of_annotations = (
            10  # TODO: Put this in a config file, no magic numbers
        )
        annotation_format_dict = {annotation_format: (annotation_re, "")}

        if not is_synchronous:  # Start a separate thread for detection annotation
            if (
                self.annotation_preview_thread
                and self.annotation_preview_thread.isRunning()
            ):
                self.annotation_preview_thread.terminate()
            kwargs = {
                "annotation_formats": annotation_format_dict,
                "files": self.files,
                "max_amount": max_amount_of_annotations,
            }
            self.annotation_preview_thread = CustomThread(
                method2run=self.annotation_detector.detect_annotations,
                signal=self.annotation_preview_signal,
                **kwargs,
            )
            self.annotation_preview_thread.start()
            return

        detected_annotations = self.annotation_detector.detect_annotations(
            self.files, annotation_format_dict, max_amount_of_annotations
        )
        return detected_annotations

    def get_dv_value_occurrences(self, dv_value: str) -> int:
        """Returns the number of occurrences of a dependent variable value in the corpora files.

        Args:
            dv_value (str): The name of the dependent variable value, that should be checked.

        Returns:
            int: The number of occurrences of the dependent variable value.
        """
        value_found = self.annotations_in_files.identifier.apply(
            lambda values: dv_value in values
        )
        return value_found.sum()

    def get_dv_values_printable(self) -> Dict[str, Tuple[int, str, str]]:
        """Returns the dependent variable values in a more readable/printable way.
        Contains the name of the dependent variable value, the number of occurrences, the parent
        dependent variable and the color.

        An example output could be:
        { "INFORMAL": (2, "FORMALITY", "#250A25"), "FORMAL": (2, "FORMALITY", "#250C21") }

        Returns:
            Dict[str, Tuple[int, str, str]]: A dictionary, where the key represents the dv-
                                    value name and the value is a tuple containing the occurrences,
                                    the parent dv and the color.
        """
        res = {}
        for dv_value in self.dependent_variable_values:
            occurrences = self.get_dv_value_occurrences(dv_value.name)
            dv_parent = dv_value.get_parent()
            if dv_parent:
                dv_parent = dv_parent.name
            color = dv_value.get_color()
            res[dv_value.name] = (occurrences, dv_parent, color)

        return res

    def update_dv_from_frontend(self, data: dict) -> None:
        """Updates the dependent variables from the frontend. The data is a dictionary,
        that contains the dependent variables and their dependent variable values with their colors.

        Example data:
        {
            'DV1': (['Var1', 'Var2'], ['#FF0000', '#ffff7f']),
            'DV2': (['Val3'], ['#0000FF'])
        }

        Args:
            data (dict): The data, that contains the dependent variables and their dependent variable values.
        """
        # Delete all dvs
        for dv in list(self.dependent_variables.keys()):
            self.remove_dv(dv)

        # Add the dvs from the data
        for dv_name, (dv_values, colors) in data.items():
            # Update the colors
            for dv_value, color in zip(dv_values, colors):
                self.set_dv_value_color(dv_value, color)

            # Add the dv
            self.add_dv(dv_name, dv_values)

        # Emit the signal for the frontend, that the dvs have changed
        self.dv_changed_signal.emit(self.get_dv_printable())
        self.dv_values_changed_signal.emit(self.get_dv_values_printable())

    def update_dv_values_from_frontend(self, data: dict) -> None:
        """Updates the dependent variable values from the frontend. The data is a dictionary,
        that contains as a key the name of the dependent variable value. The value is a tuple,
        that contains the number of occurrences, the color and the parent dependent variable.
        No color or no parent dependent variable is indicated by None.

        Example data:
        {
            "INFORMAL": (2, "FORMALITY", "#250A25"),
            "FORMAL": (2, "FORMALITY", "#250C21")
        }

        Args:
            data (dict): The data, that contains the dependent variable values and their occurrences, colors and parent dv.
        """
        # Delete all dvs
        for dv in list(self.dependent_variables.keys()):
            self.remove_dv(dv)

        # Reset the dv-values
        self.dependent_variable_values = []

        # Add the dvs from the data
        for dv_value_name, (occurrences, dv_parent, color) in data.items():
            self.add_dv_value(dv_value_name, color)

            if not dv_parent:
                continue
            dv_value = self.get_dv_value(dv_value_name)
            if not self.exists_dv(dv_parent):
                self.add_dv(dv_parent)

            dv = self.get_dv(dv_parent)
            dv.add_variable_value(dv_value)

        # Emit the signal for the frontend, that the dvs have changed
        self.dv_changed_signal.emit(self.get_dv_printable())
        self.dv_values_changed_signal.emit(self.get_dv_values_printable())

    def exists_dv(self, dv_name: str) -> bool:
        """Checks, if a dependent variable already exists in the project.

        Args:
            dv_name (str): The name of the dependent variable, that should be checked.

        Returns:
            bool: True, if the dependent variable already exists, else False.
        """
        return dv_name in self.dependent_variables

    def get_dv(self, dv_name: str) -> Variable:
        """Returns a dependent variable with the given name. If no dependent variable with the
        given name was found, the method returns None.

        Args:
            dv_name (str): The name of the dependent variable, that should be returned.

        Returns:
            Variable: The dependent variable with the given name. If no dependent variable was found, return None.
        """
        if dv_name in self.dependent_variables:
            return self.dependent_variables[dv_name]
        return None

    def remove_dv(self, dv_name: str) -> None:
        """Removes a dependent variable from the project. Also removes the reference
        from the dv-values to the dv (But will not delete the assigned dv-values).
        Will fail, if no dv with the given name was found.

        Args:
            dv_name (str): The name of the dv, that should be deleted
        """
        # Check, if the dv exists
        if dv_name not in self.dependent_variables:
            self.error_occurred_signal.emit(
                f'The Dependent Variable with the name "{dv_name}" was not found!'
            )
            return

        # Get the dv and delete the reference from his dv-values to him
        dv = self.dependent_variables[dv_name]
        for dv_value in dv.get_variable_values().copy():
            self.remove_dv_value_from_dv(dv_name, dv_value.get_name())

        # Delete the dv itself
        del self.dependent_variables[dv_name]

    def get_parent_name_of_dv_value(self, dv_value_name: str) -> str:
        """Returns the name of the parent dependent variable of a dependent variable value.

        Args:
            dv_value_name (str): The name of the dependent variable value.

        Returns:
            str: The name of the parent dependent variable of the dependent variable value.
        """
        dv_value = self.get_dv_value(dv_value_name)
        if not dv_value:
            return None
        dv_parent = dv_value.get_parent()
        if not dv_parent:
            return None
        return dv_parent.get_name()

    def get_speaker_from_text_position(
        self, file_name: str, start: int, end: int
    ) -> str:
        """Returns the speaker, that is speaking at the given text position.

        Args:
            file_name (str): The name of the file, that contains the text position.
            start (int): The start position of the text.
            end (int): The end position of the text.

        Returns:
            str: The name of the speaker, that is speaking at the given text position.
        """
        detected_speakers = self.get_detected_speakers()
        relevant_rows = (
            (detected_speakers["spoken_text_start"] <= start)
            & (detected_speakers["spoken_text_end"] >= end)
            & (detected_speakers["file_name"] == file_name)
        )
        speakers = detected_speakers[relevant_rows]["speaker_name"].values
        if len(speakers) == 0:  # No speaker was found
            return None
        elif (
            len(speakers) == 1
        ):  # Exactly one speaker was found. This is the expected case
            return speakers[0]
        return speakers  # Multiple speakers were found. Might occur, if the text position is in a overlap of two speakers

    def get_dv_printable(self) -> Dict[str, Tuple[List[str], List[str]]]:
        """Returns the dependent variables in a more readable/printable way.
        An example output could be:
        { "DV1": (["VAL1", "VAL2"], ["#250A25", "#250A25"]), "DV2": (["VAL1", "VAL2"], ["#250A25", "#250A25"]) }

        Returns:
            Dict[str, List[List[str], List[str]]]: A dictionary, where the key represents the dv-
                                  name and the value is a 2D-list containing the dv-values and the colors.
        """
        res = {}
        for dv_name, dv in self.dependent_variables.items():
            dv_values = []
            colors = []
            for dv_value in dv.get_variable_values():
                dv_values.append(dv_value.name)
                colors.append(dv_value.get_color())
            res[dv_name] = (dv_values, colors)
        return res

    def exists_dv_value(self, dv_value: str | VariableValue) -> bool:
        """Checks, if a dependent variable value already exists in the project.

        Args:
            dv_value (str | VariableValue): The name of the dependent variable value, that should be checked.

        Returns:
            bool: True, if the dependent variable value already exists, else False.
        """
        # TODO: Überlegung ist hier, ob DV-Values nicht ein dict mit name:DV-Value sein sollte? Oder man schaftt es irgendwie, mittels der __repr methode, dass der Ausdruck "dv-name in self.dependend_variable_values" funktioniert
        if type(dv_value == VariableValue):
            return dv_value in self.dependent_variable_values

        for current_dv_value in self.dependent_variable_values:
            if dv_value == current_dv_value.name:
                return True

        return False

    def exists_dv_value(self, dv_value: str | VariableValue) -> bool:
        """Checks, if a dependent variable value already exists in the project.

        Args:
            dv_value (str | VariableValue): The name of the dependent variable value, that should be checked.

        Returns:
            bool: True, if the dependent variable value already exists, else False.
        """
        if type(dv_value) == VariableValue:
            return dv_value in self.dependent_variable_values

        for current_dv_value in self.dependent_variable_values:
            if dv_value == current_dv_value.name:
                return True
        return False

    def add_dv_value(self, dv_value: str, color: str = None) -> None:
        """Adds a new dependent variable value to the project. Fails, if the dependent variable value
        already exists.

        Args:
            dv_value (str): The name of the dependent variable value, that should be added.
            color (str, optional): The color, that should be assigned to the dependent variable value. Defaults to None.
        """
        if self.exists_dv_value(dv_value):
            self.error_occurred_signal.emit(
                f'The dependent variable value "{dv_value}" already exists!'
            )
            return
        self.dependent_variable_values.append(VariableValue(name=dv_value, color=color))

    def set_dv_value_color(self, dv_value: str, color: str) -> None:
        """Sets the color of a dependent variable value. Fails, if the dependent variable value
        doesn't exist.

        Args:
            dv_value (str): The name of the dependent variable value, that should be colored.
            color (str): The color, that should be assigned to the dependent variable value.
        """
        if not self.exists_dv_value(dv_value):
            self.error_occurred_signal.emit(
                f'The dependent variable value "{dv_value}" was not found and could not be colored!'
            )
            return

        dv_value = self.get_dv_value(dv_value)
        dv_value.set_color(color)

    def remove_dv_value(self, dv_value: str | VariableValue) -> None:
        """Removes a dependent variable value from the project. Fails, if the dependent variable value
        doesn't exist.

        Args:
            dv_value (str | VariableValue): The name of the dependent variable value, that should be removed.
        """
        if not self.exists_dv_value(dv_value):
            self.error_occurred_signal.emit(
                f'The dependent variable value "{dv_value}" was not found and could not be removed!'
            )
            return

        if type(dv_value) == str:
            dv_value = self.get_dv_value(dv_value)

        # Remove the dependent variable value from all dependent variables
        for dv in self.dependent_variables.values():
            if dv_value in dv.get_variable_values():
                dv.remove_variable_value(dv_value)

        # Remove the dependent variable value from the list of dependent variable values
        self.dependent_variable_values.remove(dv_value)

    def get_dv_value(self, dv_value: str) -> VariableValue:
        """Returns a dependent variable value with the given name. If no dependent variable value with the
        given name was found, the method returns None.

        Args:
            dv_value (str): The name of the dependent variable value, that should be returned.

        Returns:
            VariableValue: The dependent variable value with the given name. If no dependent variable value was found, return None.
        """
        for current_dv_value in self.dependent_variable_values:
            if dv_value == current_dv_value.name:
                return current_dv_value
        return None

    def add_dv(self, dv_name: str, dv_values: List[str] = None) -> None:
        """Creates a new dependent variable (dv) and adds it to the project. If a dv with the same name
        already exists, the creation of the new dv will fail.

        Args:
            dv_name (str): The name of the dv. Each dv must have a unique name.
            dv_values (List[str], optional): A list of dv-values, that will automatically be assigned
                                             to the newly created dv-object. Defaults to None.
        """
        if dv_name in self.dependent_variables:
            self.error_occurred_signal.emit(
                f'The dependent variable "{dv_name}" does already exist!'
            )
            return

        # Create the dv
        self.dependent_variables[dv_name] = Variable(dv_name)

        # If there are no dv-values, return
        if not dv_values:
            return

        # Add the dv-values to the dv
        for dv_value in dv_values:
            if not self.exists_dv_value(dv_value):
                self.add_dv_value(dv_value)
            self.assign_dv_value_to_dv(dv_name, dv_value)

    def assign_dv_value_to_dv(
        self, dv_name: str, dv_value: str | VariableValue
    ) -> None:
        """Assigns a dependent variable value to a dependent variable. Fails, if the dependent variable
        or the dependent variable value doesn't exist.

        Args:
            dv_name (str): The name of the dependent variable, to which the dependent variable value should be assigned.
            dv_value (str | VariableValue): The name of the dependent variable value, that should be assigned.
        """
        if dv_name not in self.dependent_variables:
            self.error_occurred_signal.emit(
                f'The dependent variable "{dv_name}" was not found!'
            )
            return

        if not self.exists_dv_value(dv_value):
            self.error_occurred_signal.emit(
                f'The dependent variable value "{dv_value}" does not exist!'
            )
            return

        if type(dv_value) == str:
            dv_value = self.get_dv_value(dv_value)

        self.dependent_variables[dv_name].add_variable_value(dv_value)

    def assign_dv_values_to_dv(self, dv_name: str, dv_values: List[str]) -> None:
        """Assigns multiple dependent variable values to a dependent variable. Fails, if the dependent variable
        or the dependent variable value doesn't exist.

        Args:
            dv_name (str): The name of the dependent variable, to which the dependent variable values should be assigned.
            dv_values (List[str]): A list of dependent variable values, that should be assigned.
        """
        if dv_name not in self.dependent_variables:
            self.error_occurred_signal.emit(
                f'The dependent variable "{dv_name}" was not found!'
            )
            return

        for dv_value in dv_values:
            if not self.exists_dv_value(dv_value):
                self.error_occurred_signal.emit(
                    f'The dependent variable value "{dv_value}" does not exist!'
                )
                return

        for dv_value in dv_values:
            self.assign_dv_value_to_dv(dv_name, dv_value)

    def remove_dv_value_from_dv(self, dv_name: str, dv_value: str) -> None:
        """Removes a dependent variable value from a dependent variable. Fails, if the dependent variable
        or the dependent variable value doesn't exist.

        Args:
            dv_name (str): The name of the dependent variable, from which the dependent variable value should be removed.
            dv_value (str): The name of the dependent variable value, that should be removed.
        """
        if dv_name not in self.dependent_variables:
            self.error_occurred_signal.emit(
                f'The dependent variable "{dv_name}" was not found!'
            )
            return

        if not self.exists_dv_value(dv_value):
            self.error_occurred_signal.emit(
                f'The dependent variable value "{dv_name}" does not exist!'
            )
            return

        if type(dv_value) == str:
            dv_value = self.get_dv_value(dv_value)

        self.dependent_variables[dv_name].remove_variable_value(dv_value)

    def add_annotation_format(
        self,
        annotation_str: str,
        regex: str = None,
        token: str | tuple = None,
        identifier: str | tuple = None,
        multiple_identifier_separator: str = None,
    ) -> None:
        """Adds a new annotation format to the annotation detector.

        Args:
            annotation_str (str): The annotation format as a string, that should be added.
            regex (str, optional): The regular expression of the annotation format. Will be automatically created if not given.
            token (str | tuple): The start and end position of the token in the annotation string. The positions are inclusive. It's also possible, to give the designation of the token.
            identifier (Tuple[int, int] | str): The start and end position of the identifier in the annotation string. The positions are inclusive. It's also possible, to give the designation of the identifier.
            multiple_identifier_separator (str, optional): The separator for multiple identifiers. Defaults to None.
        """
        if not regex:
            self.annotation_detector.add_annotation_format_token_identifier(
                annotation_str, token, identifier, multiple_identifier_separator
            )
        else:
            self.annotation_detector.add_annotation_format_regex(
                annotation_str, regex, multiple_identifier_separator
            )

    def remove_annotation_format(self, annotation_str: str) -> None:
        """Removes an annotation format from the annotation detector."""
        success = self.annotation_detector.remove_annotation_format(annotation_str)
        if not success:
            self.error_occurred_signal.emit(
                f'The annotation format "{annotation_str}" was not found and could not be removed!'
            )

    def modify_annotation_format(self):
        pass

    def get_annotation_formats_printable(self) -> Dict[str, List[str]]:
        """Returns the annotation formats in a more readable/printable way.
        An example output could be:
        { "[$TOKEN.IDENTIFIER]": ["_", "?"], "[&TOKEN.IDENTIFIER]": [] }

        Returns:
            Dict[str, List[str]]: A dictionary, where the key represents the annotation format
                                        and the value is a list containing the separator for multiple identifiers.

        """
        res = {}
        for (
            annotation_str,
            data,
        ) in self.annotation_detector.get_annotation_formats().items():
            regex, separator = data
            if not separator:
                separator_list = []
            else:
                separator_list = [symbol for symbol in separator]
            res[annotation_str] = separator_list
        return res

    def get_annotation_formats(self) -> Dict[str, Tuple[str, str]]:
        """Returns the annotation formats in a more readable/printable way.
        An example output could be:
        { "[$TOKEN.IDENTIFIER]": ("regex", "_?"), "[&TOKEN.IDENTIFIER]": ("regex", "") }

        Returns:
            Dict[str, Tuple[str, str]]: A dictionary, where the key represents the annotation format
                                        and the value is a tuple containing the regular expression of
                                        the annotation format and the separator for multiple identifiers.

        """
        res = {}
        for (
            annotation_str,
            data,
        ) in self.annotation_detector.get_annotation_formats().items():
            regex, separator = data
            res[annotation_str] = (regex, separator)
        return res

    def get_annotation_regex(self) -> Dict[str, str]:
        """Gives you a dict, where the keys are the annotation formats and the values are the regexes.

        Returns:
            Dict[str, str]: A dictionary, where the key represents the annotation format and the value is the regex.
        """
        res = {}
        for (
            annotation_str,
            data,
        ) in self.annotation_detector.get_annotation_formats().items():
            regex, separator = data
            res[annotation_str] = regex
        return res

    def update_annotation_formats_from_frontend(self, data: dict) -> None:
        """Updates the annotation formats from the frontend. The data is a dictionary, that contains
        the annotation formats as strings and separators in a list for multiple identifiers.
        An annotation format must contain the keywords "token" and "identifier".

        Example data:
        {
            "[$token.identifier]": ["_", "?"],
            "[&token.identifier]": [],
        }

        Args:
            data (dict): The data, that contains the annotation formats and separators.
        """
        # Reset the annotation formats
        self.annotation_detector.reset_annotation_formats()

        # Add the annotation formats from the data
        for annotation_str, multiple_identifier_separator in data.items():
            separator_str = None
            if len(multiple_identifier_separator) > 0:
                separator_str = "".join(multiple_identifier_separator)

            self.add_annotation_format(
                annotation_str=annotation_str,
                token="token",
                identifier="identifier",
                multiple_identifier_separator=separator_str,
            )

        # Emit the signal for the frontend, that the annotation formats have changed
        self.annotation_formats_changed_signal.emit(
            self.get_annotation_formats_printable()
        )

    def get_detected_annotations(self) -> pd.DataFrame:
        """Returns the detected annotations in the corpora files.
        The dataframe contains the following columns:

        Column name       | content                                       | type  |\n
        token             | The word that is annotated                    | str   |\n
        identifier        | The variable values of the annotated word     | list  |\n
        annotation_start  | start position of annotation (start inclusive)| int   |\n
        annotation_end    | end position of annotation (end inclusive)    | int   |\n
        annotation_string | The annotation format that was used           | str   |\n
        file_name         | name of file where speaker was found          | str   |\n
        file_version      | version of the file                           | float |

        Returns:
            pd.DataFrame: The detected annotations in the corpora files.
        """
        return self.annotations_in_files.copy()

    def load_n_variables_with_annotation_format():
        pass

    def get_context_from_text_position(
        self, file_name: str, start: int, end: int
    ) -> str:
        """Returns the context of a text position. The context is the text, that is spoken before and after
        the text position.

        Args:
            file_name (str): The name of the file, that contains the text position.
            start (int): The start position of the text.
            end (int): The end position of the text.

        Returns:
            str: The context of the text position.
        """
        pass
        # TODO: Implement this method

    def get_count_of_unassigned_words(self) -> dict:
        """Tells the total amount of words, that could not be assigned
        to a speaker. Also specifies, how many words in each file could not be
        assigned to a speaker.

        Returns:
            dict: Contains two key-values: "Words_Total" contains the amount of
            unassigned words, while "Words_Data" separates those between files.
        """
        pass  # TODO

    def add_worker_thread(
        self,
        target: callable,
        result_signal: Signal,
        args: tuple = (),
        kwargs: dict = {},
    ) -> None:
        """Adds a worker thread to the project which executes the given target function.
        The result of the target function can be collected with the given result signal.
        The worker thread is stored in the list "worker_threads" and will be removed
        automatically, when the thread is finished.

        Args:
            target (callable): The function, that should be executed in the worker thread.
            result_signal (Signal): The signal, that should be used to send the result of the worker thread.
            args (tuple, optional): Possible args for the target function. Defaults to None.
            kwargs (dict, optional): Possible kwargs for the target function. Defaults to None.
        """
        worker_thread = CustomThread(
            method2run=target, signal=result_signal, *args, **kwargs
        )
        worker_thread.finished.connect(lambda: self.remove_worker_thread(worker_thread))
        self.worker_threads.append(worker_thread)
        worker_thread.start()

    def remove_worker_thread(self, worker_thread: CustomThread) -> None:
        """Removes a worker thread from the list of worker threads.

        Args:
            worker_thread (CustomThread): The worker thread, that should be removed.
        """
        if worker_thread.isRunning():
            worker_thread.quit()

        if worker_thread in self.worker_threads:
            self.worker_threads.remove(worker_thread)

    def remove_all_worker_threads(self) -> None:
        """Removes all worker threads from the list of worker threads."""
        for worker_thread in self.worker_threads:
            if worker_thread.isRunning():
                worker_thread.quit()
        self.worker_threads = []

    def create_datasets(
        self, files: List[File] = None, is_synchronous: bool = False
    ) -> None | dict:
        """Creates datasets from the corpora files. The resulting data is send
        via the 'corpus_analysis_data_signal'.

        Args:
            files (List[File], optional): User can specify which files should be used for analysis. Defaults to None.
            is_synchronous (bool, optional): If the method is executed in an extra thread. Defaults to False.

        Returns:
            None | dict: If the method is called synchronous, the resulting dataframes are returned. Otherwise
                         the signal "corpus_analysis_data_signal" is emitted.
        """
        if not files:
            files = self.files
        corpus_dict = {file.path: file.content for file in files}
        iv_dict = {
            iv_name: [iv_value.name for iv_value in iv.get_variable_values()]
            for iv_name, iv in self.independent_variables.items()
        }
        dv_dict = {
            dv_name: [dv_value.name for dv_value in dv.get_variable_values()]
            for dv_name, dv in self.dependent_variables.items()
        }
        speaker_dict = {
            speaker_name: [iv_value.name for iv_value in speaker.get_iv_values()]
            for speaker_name, speaker in self.speakers.items()
        }
        speaker_re = self.speaker_detector.get_re_speaker(
            self.speaker_detector.get_speaker_format()
        )
        annotation_re_dict = self.annotation_detector.get_annotation_formats()
        regex_input = [annotation_re_dict, speaker_re, False, 10, 10]

        # Create the datasets
        self.dc_thread = DCThread(
            regex_input, corpus_dict, iv_dict, dv_dict, speaker_dict
        )
        self.dc_thread.start()

        # Handle the returned values differently depending on "is_synchronous" parameter
        if is_synchronous:
            self.dc_thread.wait()
            return self.dc_thread.results
        else:
            self.dc_thread.finished.connect(self.on_dataset_creation_finished)

    def on_dataset_creation_finished(self) -> None:
        """Is called when the thread for creating the analysis datasets of a corpus
        is finished. Emits a signal to notify the GUI, that the analysis is finished.
        """
        results = self.dc_thread.results

        # Check if an exception occurred
        if type(results) == str:
            self.error_occurred_signal.emit(results)
            self.corpus_analysis_data_signal.emit({})
            return

        # Otherwise send the result of the analysis with a signal
        self.corpus_analysis_data_signal.emit(results)

    def save_datasets(
        self,
        output_dir: str,
        results: dict,
        encoding: str = "utf-8",
        separator: str = ";",
    ) -> None:
        """Takes the results of the create_datasets method and saves them in the given output directory.

        Args:
            output_dir (str): The Folder, where the datasets should be saved.
            results (dict): The results of the create_datasets method.
            encoding (str, optional): What encoding should be used for the csv files. Defaults to "utf-8".
            separator (str, optional): What separator should be used in the csv files. Defaults to ",".
        """
        # Save the datasets
        for file_name, dataset in results.items():
            if type(dataset) == dict:
                with open(os.path.join(output_dir, file_name + ".json"), "w") as file:
                    json.dump(dataset, file)
            elif type(dataset) == pd.DataFrame:
                dataset.to_csv(
                    os.path.join(output_dir, file_name + ".csv"),
                    encoding=encoding,
                    sep=separator,
                    index=False,
                )

    def save_project_metadata(self) -> None:
        """Saves metadata for the project as a json file. Includes project
        name and description, annotation and speaker formats and the path to
        all other relevant project files.
        """
        proj_metadata_filepath = os.path.join(
            self.proj_directory, "project_metadata.json"
        )

        # Create the data for the json files
        project_dict = {
            "proj_name": self.proj_name,
            "proj_description": self.proj_description,
            "speaker_format": self.get_speaker_format(),
            "annotation_format": self.get_annotation_formats(),
            "independent_variables_filepath": os.path.join(
                self.proj_directory, "independent_variables.json"
            ),
            "dependent_variables_filepath": os.path.join(
                self.proj_directory, "dependent_variables.json"
            ),
            "speakers_filepath": os.path.join(self.proj_directory, "speakers.json"),
            "files_filepath": os.path.join(self.proj_directory, "files.json"),
            "detected_speakers_filepath": os.path.join(
                self.proj_directory, "detected_speakers.csv"
            ),
            "detected_annotations_filepath": os.path.join(
                self.proj_directory, "detected_annotations.csv"
            ),
        }
        # Save the data
        file_utils.save_json_file(proj_metadata_filepath, project_dict)

    def save_detected_speakers(self, detected_speakers: pd.DataFrame = None) -> None:
        """Saves the data of the detected speakers inside the files in a csv file.

        Args:
            detected_speakers (pd.DataFrame, optional): Dataframe containing
            the detected speakers. If not given, the detected speakers in the
            current project are used to save the data.
        """
        # Save the data
        det_speakers_filename = "detected_speakers.csv"
        det_speakers_filepath = os.path.join(self.proj_directory, det_speakers_filename)
        if detected_speakers is not None:
            detected_speakers.to_csv(det_speakers_filepath, index=False)
        else:
            self.speakers_in_files.to_csv(det_speakers_filepath, index=False)

    def save_detected_annotations(self) -> None:
        """Saves the data of the detected annotations in a csv file."""
        # Save the data
        det_annotations_filename = "detected_annotations.csv"
        det_annotations_filepath = os.path.join(
            self.proj_directory, det_annotations_filename
        )
        self.annotations_in_files.to_csv(det_annotations_filepath, index=False)

    def save_speaker_data(self) -> None:
        """Saves the data of the Speakers in a json file."""
        speakers_filename = "speakers.json"
        speakers_filepath = os.path.join(self.proj_directory, speakers_filename)
        speaker_dict = Speaker.to_dict(self.speakers.values())

        # Save the data
        file_utils.save_json_file(speakers_filepath, speaker_dict)

    def save_iv_data(self) -> None:
        """Saves the data of the independent variables in a json file."""
        iv_filename = "independent_variables.json"
        iv_filepath = os.path.join(self.proj_directory, iv_filename)
        independent_variable_dict = Variable.to_dict(
            self.independent_variables.values()
        )

        # Save the data
        file_utils.save_json_file(iv_filepath, independent_variable_dict)

    def save_dv_data(self) -> None:
        """Saves the data of the dependent variables in a json file."""
        dv_filename = "dependent_variables.json"
        dv_filepath = os.path.join(self.proj_directory, dv_filename)
        dependent_variable_dict = Variable.to_dict(self.dependent_variables.values())
        dependent_variable_dict["VariableValues"] = [
            dv_value.name for dv_value in self.dependent_variable_values
        ]

        # Save the data
        file_utils.save_json_file(dv_filepath, dependent_variable_dict)

    def save_file_data(self) -> None:
        """Saves the data of the corpora files in a json file."""
        # Get the current data
        file_dict = File.to_dict(self.files)

        # Save the data
        files_filename = "files.json"
        files_filepath = os.path.join(self.proj_directory, files_filename)
        file_utils.save_json_file(files_filepath, file_dict)

    def save_project(self, proj_path: str) -> None:
        """Saves the project in a given directory. The name of the directory is
        equivalent to the project name. The project is saved as the following files:
            - project_metadata.json: Contains the project name and description
            - independent_variables.json: Contains the independent variables
            - dependent_variables.json: Contains the dependent variables
            - speakers.json: Contains the speakers
            - files.json: Contains the path to the corpora files

        Args:
            proj_path (str): The path, where the project should be saved.
        """
        if not proj_path.endswith(self.proj_name):
            proj_path = os.path.join(proj_path, self.proj_name)

        if not os.path.exists(proj_path):
            os.makedirs(proj_path)
        self.save_project_metadata()
        self.save_iv_data()
        self.save_dv_data()
        self.save_speaker_data()
        self.save_file_data()
        self.save_detected_annotations()
        self.save_detected_speakers()

    @staticmethod
    def load_project(proj_path: str, is_synchronous=False) -> "Project":
        """Loads a project from a given directory. Needs the path of the directory,
        containing the project_metadata.json file.

        Args:
            proj_path (str): The path of the directory, containing the project.
            is_synchronous (bool, optional): If set to True, the loading process is synchronous. Defaults to False.

        Returns:
            Project: The loaded project
        """
        # Load the project metadata
        project_dict = file_utils.load_json_file(
            os.path.join(proj_path, "project_metadata.json")
        )
        proj_name = project_dict["proj_name"]
        proj_description = project_dict["proj_description"]
        proj_speaker_format = project_dict["speaker_format"]
        proj_annotation_formats = project_dict["annotation_format"]

        # Load the independent variables
        independent_variable_dict = file_utils.load_json_file(
            project_dict["independent_variables_filepath"]
        )

        # Load the dependent variables
        dependent_variable_dict = file_utils.load_json_file(
            project_dict["dependent_variables_filepath"]
        )

        # Load the speakers
        speaker_dict = file_utils.load_json_file(project_dict["speakers_filepath"])

        # Load the information about the files
        file_dict = file_utils.load_json_file(project_dict["files_filepath"])

        # Load the detected speakers
        detected_speakers = pd.read_csv(project_dict["detected_speakers_filepath"])

        # Load the detected annotations
        detected_annotations = pd.read_csv(
            project_dict["detected_annotations_filepath"]
        )
        detected_annotations["identifier"] = detected_annotations.identifier.apply(
            ast.literal_eval
        )

        independent_variables = {}
        dependent_variables = {}
        dependent_variable_values = []
        speakers = {}
        files = []

        # Create the independent variables
        for variable in independent_variable_dict["Variables"]:
            iv_name = variable["Name"]
            iv = Variable(iv_name)
            for iv_value in variable["VariableValues"]:
                iv_value_name = iv_value["Name"]
                iv_value_color = iv_value["Color"]
                iv.add_variable_value(VariableValue(iv_value_name, iv_value_color))
            independent_variables[iv_name] = iv

        # Create the dependent variables
        added_values = set()
        for variable in dependent_variable_dict["Variables"]:
            dv_name = variable["Name"]
            dv = Variable(dv_name)

            for dv_value in variable["VariableValues"]:
                dv_value_name = dv_value["Name"]
                dv_value_color = dv_value["Color"]
                dv_value = VariableValue(name=dv_value_name, color=dv_value_color)
                dv.add_variable_value(dv_value)
                dependent_variable_values.append(dv_value)
                added_values.add(dv_value_name)
            dependent_variables[dv_name] = dv

        for dv_value in dependent_variable_dict["VariableValues"]:
            if not dv_value in added_values:
                dependent_variable_values.append(VariableValue(dv_value))
                added_values.add(dv_value)

        # Create the speakers
        for speaker in speaker_dict["Speakers"]:
            speaker_name = speaker["Name"]
            speaker_color = speaker["Color"]
            s = Speaker(name=speaker_name, color=speaker_color)
            for iv_name, iv_value in speaker["Variables"].items():
                iv = independent_variables[iv_name]
                iv_value = iv.get_variable_value(iv_value)
                s.add_iv_value(iv_value)
            speakers[speaker_name] = s

        # Check, if the files were modified or moved. If so, the files are not loaded
        for file in file_dict["Files"]:
            for file_name, file_data in file.items():
                file = File(
                    file_name=file_name,
                    encoding=file_data["encoding"],
                    file_path=file_data["path"],
                    file_version=file_data["version"],
                )
                if file.was_file_moved():
                    # TODO: Implement a method to handle moved files
                    continue
                files.append(file)

        # Create the project
        project = Project(proj_name, proj_description, os.path.split(proj_path)[0])

        # Update the files:
        project.update_files(files, is_synchronous=is_synchronous)

        project.independent_variables = independent_variables
        project.dependent_variables = dependent_variables
        project.dependent_variable_values = dependent_variable_values
        project.speakers = speakers
        project.speakers_in_files = detected_speakers
        project.annotations_in_files = detected_annotations
        project.set_speaker_format(proj_speaker_format)
        for annotation_format, annotation_data in proj_annotation_formats.items():
            project.add_annotation_format(
                annotation_str=annotation_format,
                regex=annotation_data[0],
                multiple_identifier_separator=annotation_data[1],
            )
        return project

    def send_update_to_frontend(self) -> None:
        """Sends out all signals that are used to update the view."""
        # Send signals to update the view
        for file in self.files:
            self.file_added_signal.emit(file)
        self.iv_changed_signal.emit(self.get_iv_printable())
        self.speaker_changed_signal.emit(self.get_speakers_printable())
        self.dv_changed_signal.emit(self.get_dv_printable())
        self.dv_values_changed_signal.emit(self.get_dv_values_printable())
        self.annotation_formats_changed_signal.emit(
            self.get_annotation_formats_printable()
        )
