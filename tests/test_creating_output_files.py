import unittest
from src.model.corpus_compass_model import Project
from src.model.variables_speakers import Variable, VariableValue, Speaker
from src.model.files import File
import os


class GetOutputFilesTestCase(unittest.TestCase):
    def test_creating_main_dataset_german(self):
        """Test if the main dataset can be created correctly"""
        project = Project("Testproject")

        # project.load_files(["./tests/test_data/Carsten.txt"], is_synchronous=True)
        # Add some files to the project
        file_content = "SpeakerA: Ich gehe heute zur [$UniBib.DE+UNIWORD], um dort an meinem [$Masterprojekt.DE+UNIWORD] weiterarbeiten.\nSpeakerB: Ach [$schön.DE]! \nSpeakerA: Übrigens, wusstest du, dass dieses Gespräch aufgenommen und [$analysiert.UNBEKANNTEVARIABLE] wird? \nSpeakerB: Na klar, deshalb sag ich mal das Wort UniBib, damit der Nutzer ein Beispiel für ein Nicht-markiertes Wort hat"

        f1 = File(
            "File1",
            "utf8",
            "./tests/test_data/TestProject/file1.txt",
            1.0,
            file_content,
        )
        project.add_file(f1)

        project.add_annotation_format(
            annotation_str="[$TOKEN.IDENTIFIER]",
            token="TOKEN",
            identifier="IDENTIFIER",
            multiple_identifier_separator="+",
        )
        project.detect_annotations()

        # Group the detected annotations to a dependent variable
        project.add_dv("university")
        project.assign_dv_value_to_dv("university", "UNI_WORD")
        project.add_dv("german")
        project.assign_dv_value_to_dv("german", "DE")

        # Detect the speakers in the file
        project.set_speaker_format("CUSTOM", r"(?P<name>^[A-z0-9?._]+): ")
        project.detect_speakers()

        # Add some independent variables to the speakers
        project.add_iv("Age", ["Old", "Young"])
        project.add_iv("Gender", ["Male", "Female"])
        project.assign_iv_value_to_speaker("SpeakerA", "Age", "Young")
        project.assign_iv_value_to_speaker("SpeakerA", "Gender", "Male")
        project.assign_iv_value_to_speaker("SpeakerB", "Age", "Old")
        project.assign_iv_value_to_speaker("SpeakerB", "Gender", "Male")

        # Create the main dataset
        results = project.create_datasets(is_synchronous=True)

        # Save the datasets
        os.makedirs("./tests/test_data/TestOutputGerman", exist_ok=True)
        project.save_datasets(
            "./tests/test_data/TestOutputGerman",
            results,
            encoding="cp1252",
            separator=";",
        )
