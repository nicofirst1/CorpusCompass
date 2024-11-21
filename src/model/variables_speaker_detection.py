from enum import Enum
from src.model.files import File
from PySide6.QtCore import Signal, QThread, QObject, SIGNAL
from typing import List, Dict, Tuple
import pandas as pd
import re


class SpeakerFormats(Enum):
    """Enum that contains the currently supported Speaker Formats
    """
    STANDARD = "STANDARD"
    PRAAT = "PRAAT"
    ELAN = "ELAN"
    FLEX = "FLEX"
    CUSTOM = "CUSTOM"


class SpeakerDetector(QObject):
    """Class that can find the speaker name and the text that is spoken by a 
    speaker in a corpora/file. The speaker format provides the speaker detection
    a regular expression, on how to detect the speaker.
    """
    def __init__(self, current_format: SpeakerFormats = SpeakerFormats.STANDARD) -> None:
        super().__init__()
        self.current_format: SpeakerFormats = current_format
        self.custom_format: str = None
    
    def detect_speakers(self, files: List[File], speaker_format: str | SpeakerFormats = None) -> pd.DataFrame | None:
        """Searches in one or multiple files for speakers and their spoken text.
        Returns the results as a dataframe with the following structure:

        Column name       | content                              | type  |\n
        speaker_name      | name of the speaker                  | str   |\n
        speaker_start     | start position of speaker name       | int   |\n
        speaker_end       | end position of speaker name         | int   |\n
        spoken_text_start | start position of the spoken text    | int   |\n
        spoken_text_end   | end position of the spoken text      | int   |\n
        file_name         | name of file where speaker was found | str   |\n
        file_version      | version of the file                  | float |

        Start- and end-positions of the speaker and the spoken text are both 
        inclusive.

        Args:
            files (List[File]): A list of files, in which the method should search
                                for speakers

        Returns:
            pd.DataFrame: Contains the detected speakers
        """
        if not speaker_format:
            speaker_format = self.current_format

        # Get the regular expression which is used to detect speakers
        re_speaker = self.get_re_speaker(speaker_format)

        # Set up the dataframe, that will contain the detected speaker info
        type_conversion_dict = {'speaker_name': str, 'speaker_start': int, 'speaker_end': int, 'spoken_text_start': int, 'spoken_text_end': int, 'file_name': str, 'file_version': float}
        detected_speakers_df = pd.DataFrame(columns=["speaker_name", "speaker_start", "speaker_end", "spoken_text_start", "spoken_text_end", "file_name", "file_version"])
        detected_speakers_df = detected_speakers_df.astype(type_conversion_dict)

        # Search for speakers in every file provided
        for file in files:
            # Method returns all matches for speakers in the text
            detected_speakers = re.finditer(re_speaker, file.content)

            # Put the matches and additional info in a dataframe
            data = [(detected_speaker.group("name"), detected_speaker.span()[0], detected_speaker.span()[1]) for detected_speaker in detected_speakers]
            temp_df = pd.DataFrame(data, columns=["speaker_name", "speaker_start", "speaker_end"])
            temp_df["spoken_text_start"] = temp_df["speaker_end"] + 1
            temp_df["spoken_text_end"] = temp_df["speaker_start"].shift(-1, fill_value=file.number_of_chars) - 1
            temp_df["file_name"] = file.name
            temp_df["file_version"] = file.version
            # Add detected speaker for the current file to the result-dataframe
            detected_speakers_df = pd.concat([detected_speakers_df, temp_df], ignore_index=True)
        return detected_speakers_df
    
    def set_speaker_format(self, new_format: SpeakerFormats | str, custom_format: str = None) -> None:
        if type(new_format) == str:
            new_format = SpeakerFormats(new_format)
        self.current_format = new_format

        if new_format == SpeakerFormats.CUSTOM:
            self.custom_format = custom_format
    
    def get_speaker_format(self) -> SpeakerFormats:
        return self.current_format
    
    def get_speaker_format_str(self) -> str:
        return self.current_format.value

    def get_re_speaker(self, speaker_format: SpeakerFormats) -> str:
        # TODO: Add more supported formats
        if speaker_format == SpeakerFormats.STANDARD:
            # \w stands for word characters, which include a-z,A-Z,0-9 and the underscore character _
            return r"(?P<name>\w+(\s\w+)?):"
        elif speaker_format == SpeakerFormats.CUSTOM:
            return self.custom_format
        elif speaker_format != None:
            return r"(?P<name>\w+(\s\w+)?):" # TODO: Should be deleted later, is only used for debugging
        else:
            raise NotImplementedError(f'The given Speaker Format "{self.speaker_format}" is currently not supported!')


class AnnotationDetector():
    """Class that can find annotations in a corpora/file. The annotation format
    provides the annotation detection a regular expression, on how to detect the
    annotation. The annotation can contain multiple identifiers, which are separated
    by a separator. The separator is also provided in the annotation format.
    """

    def __init__(self, annotation_formats: Dict[str, Tuple[str, str]] = None) -> None:
        """Initializes the AnnotationDetector with the given annotation formats.

        Args:
            annotation_formats (Dict[str, Tuple[str, str]], optional): A dictionary that contains the annotation formats.
            The key contains the annotation format as a string, the value is a tuple that contains the regular expression 
            and the separator for multiple identifiers. Defaults to None.
        """
        if annotation_formats:
            self.annotation_formats = annotation_formats
        else:
            self.annotation_formats = {}

    def detect_annotations(self, files: List[File], annotation_formats: Dict[str, Tuple[str, str]] = None, max_amount: int = None) -> pd.DataFrame:
        """Searches in one or multiple files for annotations and their spoken text.
        Returns the results as a dataframe with the following structure:

        Column name       | content                                       | type  |\n
        token             | The word that is annotated                    | str   |\n
        identifier        | The variable values of the annotated word     | list  |\n
        annotation_start  | start position of annotation (start inclusive)| int   |\n
        annotation_end    | end position of annotation (end inclusive)    | int   |\n
        annotation_string | The annotation format that was used           | str   |\n
        file_name         | name of file where speaker was found          | str   |\n
        file_version      | version of the file                           | float |

        Start- and end-positions of the annotation are both inclusive.

        Args:
            files (List[File]): A list of files, in which the method should search
                                for speakers
            annotation_formats (Dict[str, Tuple[str, str]], optional): A dictionary, in which
                                the annotation formats are defined. The key contains the annotation
                                format as a string, the value is a tuple that contains the regular expression
                                and the separator for multiple identifiers. If not provided, the detector
                                uses all annotation formats that are saved in the annotation_formats attribute.
            max_amount (int, optional): After detecting the given amount of annotations, the method stops
                                searching for more annotations. If not provided, the method searches for all
                                annotations in the files.

        Returns:
            pd.DataFrame: Contains the detected speakers
        """
        detected_annotations_df = pd.DataFrame(columns=["token", "identifier", "annotation_start", "annotation_end", "annotation_string", "file_name", "file_version"])
        type_conversion_dict = {'token': str, 'identifier': object, 'annotation_start': int, 'annotation_end': int, 'annotation_string': str, 'file_name': str, 'file_version': float}
        detected_annotations_df = detected_annotations_df.astype(type_conversion_dict)
        if not annotation_formats:
            annotation_formats = self.annotation_formats

        for file in files:
            for annotation_str, annotation_format in annotation_formats.items():
                # Check if the maximum amount of annotations is reached
                if max_amount and len(detected_annotations_df) >= max_amount:
                    detected_annotations_df = detected_annotations_df.head(max_amount)
                    break
                
                # Detect the annotations in the file and add them to the dataframe
                re_annotation, annotation_separator = annotation_format
                temp_df = self.detect_annotations_in_file(file, annotation_str, re_annotation, annotation_separator, max_amount)
                detected_annotations_df = pd.concat([detected_annotations_df, temp_df], ignore_index=True)
        
        return detected_annotations_df

    def detect_annotations_in_file(self, file: File, annot_str: str, annot_re: str, annot_sep: str, max_amount: int = None) -> pd.DataFrame:
        """Detects annotations in a single file.

        Args:
            file (File): The file in which the annotations should be detected
            annot_str (str): How the annotation format looks like, e.g. "[$token.identifier]"
            annot_re (str): The regular expression that is used to detect the annotation, e.g. r"\\[$(?P<token>\\w+)\\.(?P<identifier>\\w+)\\]"
            annot_sep (str): The separator for multiple identifiers, e.g. "_"
            max_amount (int, optional): After detecting the given amount of annotations, the method stops
                                searching for more annotations. If not provided, the method searches for all
                                annotations in the files.

        Returns:
            pd.DataFrame: Contains the detected annotations
        """
        # Find all annotations using the regular expression
        detected_annotations = re.finditer(annot_re, file.content)
        
        # Put the matches and additional info in a dataframe
        data = []
        counter = 0
        for detected_annotation in detected_annotations:
            counter += 1
            data.append((detected_annotation.group("token"), detected_annotation.group("identifier"), detected_annotation.span()[0], detected_annotation.span()[1]))
            if max_amount and counter >= max_amount:
                break
        detected_annot_df = pd.DataFrame(data, columns=["token", "identifier", "annotation_start", "annotation_end"])
        # Put the identifiers in a list (can be multiple)
        if annot_sep != "":
            detected_annot_df["identifier"] = detected_annot_df["identifier"].str.split(annot_sep)
        else:
            detected_annot_df["identifier"] = detected_annot_df["identifier"].apply(lambda x: [x])
        # Add additional information to the dataframe
        detected_annot_df["annotation_string"] = annot_str
        detected_annot_df["file_name"] = file.name
        detected_annot_df["file_version"] = file.version

        return detected_annot_df

    def get_annotation_format(self, annotation_format_str: str) -> Tuple[str, str]:
        """Returns the regular expression and the separator for multiple identifiers
        of the given annotation format.

        Args:
            annotation_format_str (str): The annotation format as a string

        Returns:
            Tuple[str, str]: The regular expression and the separator for multiple identifiers
        """
        if annotation_format_str in self.annotation_formats:
            return self.annotation_formats[annotation_format_str]
        return None
    
    def get_annotation_formats(self) -> Dict[str, Tuple[str, str]]:
        """Returns all annotation formats that are currently supported.

        Returns:
            Dict[str, Tuple[str, str]]: A dictionary that contains the annotation formats
            as keys and the regular expression and the separator for multiple identifiers as values.
        """
        return self.annotation_formats
    
    def add_backslash_to_re_characters(self, string: str) -> str:
        """Adds a backslash to all characters that are used in regular expressions.

        Args:
            string (str): The string, where characters in regular expressions should be escaped

        Returns:
            str: The escaped string
        """
        characters_to_replace = list(r"\.[]^$*+?{}|()")
        for char in characters_to_replace:
            string = string.replace(char, "\\" + char)
        return string

    def remove_annotation_format(self, annotation_str: str) -> bool:
        """Removes an annotation format from the annotation formats.

        Args:
            annotation_str (str): The annotation format as a string

        Returns:
            bool: True, if the annotation format was removed successfully. False, if the annotation format is not in the annotation formats.
        """
        if annotation_str in self.annotation_formats:
            del self.annotation_formats[annotation_str]
            return True
        return False
    
    def add_annotation_format_regex(self, annotation_str: str, annotation_re: str, multiple_identifier_separator: str = None) -> bool:
        """Adds a new annotation format to the annotation formats. The annotation format
        is defined by the annotation string and the regular expression. The annotation format
        can contain multiple identifiers, which are separated by a separator. The separator
        is also provided in the annotation format.

        Args:
            annotation_str (str): The annotation format as a string (e.g. "[$token.identifier]")
            annotation_re (str): The regular expression that is used to detect the annotation
            multiple_identifier_separator (str, optional): The separator for multiple identifiers. Defaults to None.

        Returns:
            bool: True, if the annotation format was added successfully. False, if the annotation format is already in the annotation formats.
        """
        if annotation_str in self.annotation_formats:
            return False
        
        if not multiple_identifier_separator:
            multiple_identifier_separator = ""
        
        self.annotation_formats[annotation_str] = (annotation_re, multiple_identifier_separator)
        return True

    def get_regex_from_annotation_format(self, 
                                         annotation_str: str,
                                         token: Tuple[int, int]| str,
                                         identifier: Tuple[int, int] | str,
                                         multiple_identifier_separator: str = None) -> str:
        """Creates a regular expression from an annotation format. The annotation format
        is defined by the annotation string, the position of the token and the identifier
        in the annotation string. The annotation format can contain multiple identifiers,
        which are separated by a separator. The separator is also provided in the annotation
        format.

        Example: We annotate like this: "This is a [$annotation.VAR1_VAR2_VAR3]."
        The annotation string is "[$token.identifier]"
        The token position is (1, 5)
        The identifier position is (7, 15)
        The multiple identifier separator is "_"	

        Args:
            annotation_str (str): The annotation format as a string
            token (Tuple[int, int] | str): The start and end position of the token in the annotation string. The positions are inclusive. It's also possible, to give the designation of the token.
            identifier (Tuple[int, int] | str): The start and end position of the identifier in the annotation string. The positions are inclusive. It's also possible, to give the designation of the identifier.
            multiple_identifier_separator (str, optional): The separator for multiple identifiers. Defaults to None.

        Returns:
            (raw) str: The regular expression for the annotation
        """
        # Check if the token and identifier are given as a string or as a position
        token_pos = token
        identifier_pos = identifier

        # If the token and identifier are given as a string, we have to find the position of the token and identifier in the annotation string
        if type(token) == str:
            token_start = annotation_str.find(token)
            token_end = token_start + len(token) - 1
            token_pos = (token_start, token_end)
        
        if type(identifier) == str:
            identifier_start = annotation_str.find(identifier)
            identifier_end = identifier_start + len(identifier) - 1
            identifier_pos = (identifier_start, identifier_end)

        # Check if the token is before the identifier or the identifier is before the token
        token_before_identifier = token_pos[0] < identifier_pos[0]

        first_pos = token_pos if token_before_identifier else identifier_pos
        second_pos = identifier_pos if token_before_identifier else token_pos

        # Split the annotation string into prefix, infix and suffix, separated by the token and identifier
        prefix = annotation_str[ : first_pos[0]]
        infix = annotation_str[first_pos[1] + 1 : second_pos[0]]
        suffix = annotation_str[second_pos[1] + 1 : ]

        prefix = self.add_backslash_to_re_characters(prefix)
        infix = self.add_backslash_to_re_characters(infix)
        suffix = self.add_backslash_to_re_characters(suffix)

        # Create the regular expression for the annotation
        token_re = r"(?P<token>\w+)"
        if multiple_identifier_separator:
            multiple_identifier_separator_backslash = self.add_backslash_to_re_characters(multiple_identifier_separator)
            identifier_re = r"(?P<identifier>\w+(" + multiple_identifier_separator_backslash +  r"\w+)*)"
        else:
            multiple_identifier_separator = ""
            identifier_re = r"(?P<identifier>\w+)"

        if token_before_identifier:
            annotation_re = prefix + token_re + infix + identifier_re + suffix
        else:
            annotation_re = prefix + identifier_re + infix + token_re + suffix
        return annotation_re

    def add_annotation_format_token_identifier(self, 
                                               annotation_str: str,
                                               token: Tuple[int, int]| str,
                                               identifier: Tuple[int, int] | str,
                                               multiple_identifier_separator: str = None) -> bool:
        """Adds a new annotation format to the annotation formats. The annotation format
        is defined by the annotation string, the position of the token and the identifier
        in the annotation string. The annotation format can contain multiple identifiers,
        which are separated by a separator. The separator is also provided in the annotation
        format.

        Example: We annotate like this: "This is a [$annotation.VAR1_VAR2_VAR3]."
        The annotation string is "[$token.identifier]"
        The token position is (1, 5)
        The identifier position is (7, 15)
        The multiple identifier separator is "_"	

        Args:
            annotation_str (str): The annotation format as a string
            token (Tuple[int, int] | str): The start and end position of the token in the annotation string. The positions are inclusive. It's also possible, to give the designation of the token.
            identifier (Tuple[int, int] | str): The start and end position of the identifier in the annotation string. The positions are inclusive. It's also possible, to give the designation of the identifier.
            multiple_identifier_separator (str, optional): The separator for multiple identifiers. Defaults to None.

        Returns:
            bool: True, if the annotation format was added successfully. False, if the annotation format is already in the annotation formats.
        """
        if annotation_str in self.annotation_formats:
            return False
        
        annotation_re = self.get_regex_from_annotation_format(annotation_str, token, identifier, multiple_identifier_separator)
        
        self.annotation_formats[annotation_str] = (annotation_re, multiple_identifier_separator)
        return True

    def add_annotation_format_word(self) -> str:
        # TODO: Needs implementation
        pass

    def reset_annotation_formats(self) -> None:
        """Resets the annotation formats to an empty dictionary.
        """
        self.annotation_formats = {}
