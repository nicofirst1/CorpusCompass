import unittest
from src.model.corpus_compass_model import Project
from src.model.variables_speakers import Variable, VariableValue, Speaker
from src.model.files import File


class GetOutputFilesTestCase(unittest.TestCase):
    def test_creating_main_dataset_german(self):
        """Test if the main dataset can be created correctly"""
        project = Project("Testprojekt")

        project.load_files(["./tests/test_data/Carsten.txt"], is_synchronous=True)
        project.add_annotation_format(annotation_str="[$IDENTIFIER.TOKEN]", token="TOKEN", identifier="IDENTIFIER", multiple_identifier_separator=".")
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
        project.create_datasets("./tests/test_data/TestOutputGerman", encoding="cp1252", separator=";")
    
    def test_creating_main_dataset_arabic(self):
        """Test if the main dataset can be created correctly"""
        project = Project("Testprojekt")

        project.load_files(["./tests/test_data/Adnan.txt"], is_synchronous=True)
        encoding = project.files[0].encoding
        project.add_annotation_format(annotation_str="[$IDENTIFIER.TOKEN]", token="TOKEN", identifier="IDENTIFIER", multiple_identifier_separator=".")
        project.detect_annotations()

        # Group the detected annotations to a dependent variable
        project.add_dv("Typical Iraqi-Arabic")
        project.assign_dv_value_to_dv("Typical Iraqi-Arabic", "IA")
        project.add_dv("Question word")
        project.assign_dv_value_to_dv("Question word", "Q-WORD")
        project.add_dv("Other language")
        project.assign_dv_value_to_dv("Other language", "OTH-L")
        project.add_dv("German Word")
        project.assign_dv_value_to_dv("German Word", "G")
        project.add_dv("German Context")
        project.assign_dv_values_to_dv("German Context", ["G-SCHOOL", "G-JOB", "G-FRIE", "G-COV", "G-DL", "G-OTH", "G-ZIT", "G-GER", "G-L"])
        project.add_dv("Standard Arabic")
        project.assign_dv_value_to_dv("Standard Arabic", "OTH-SA")
        project.add_dv("Words/Features other dialect")
        project.assign_dv_value_to_dv("Words/Features other dialect", "OTH-DIAL")
        project.add_dv("Andere SS")
        project.assign_dv_value_to_dv("Andere SS", "SS-DIF")
        project.add_dv("Leveling")
        project.assign_dv_value_to_dv("Leveling", "SS-LEV")
        project.add_dv("Religious Phrases")
        project.assign_dv_value_to_dv("Religious Phrases", "RELIG")
        project.add_dv("maal usage")
        project.assign_dv_values_to_dv("maal usage", ["MAAL", "NO-MAAL"])
        project.add_dv("maal major categories")
        project.assign_dv_values_to_dv("maal major categories", ["AL-N+N", "N+AL-N", "AL-N+AL-N", "N+N"])
        project.add_dv("maal mit iDaafa")
        project.assign_dv_values_to_dv("maal mit iDaafa", ["IDAAFA+N", "N+IDAAFA", "IDAAFA+IDAAFA", "IDAAFA+MAAL", "MAAL+IDAAFA"])
        project.add_dv("maal maal and pronoun")
        project.assign_dv_values_to_dv("maal maal and pronoun", ["AL-N+MAAL", "MAAL+AL-N", "N+MAAL", "MAAL-N"])
        project.add_dv("maal possessive")
        project.assign_dv_value_to_dv("maal possessive", "POSS")
        project.add_dv("maal with verb")
        project.assign_dv_values_to_dv("maal with verb", ["MAAL-V", "V-MAAL"])
        project.add_dv("maal mit DEM")
        project.assign_dv_value_to_dv("maal mit DEM", "DEM-MAAL")
        project.add_dv("maal with G word")
        project.assign_dv_value_to_dv("maal with G word", "MAAL-G")
        project.add_dv("maal desription")
        project.assign_dv_value_to_dv("maal desription", "DESCR")
        project.add_dv("maal long constructions")
        project.assign_dv_value_to_dv("maal long constructions", "LONG")
        project.add_dv("maal semnatic categories")
        project.assign_dv_values_to_dv("maal semnatic categories", ["CN", "PN"])
        project.add_dv("Präfix da-")
        project.assign_dv_value_to_dv("Präfix da-", "DA")
        project.add_dv("Demonstratives")
        project.assign_dv_values_to_dv("Demonstratives", ["DEM-HAAY", "DEM-HAAYA", "DEM-HA","DEM-DHANNI", "DEM-HAADHA"])
        project.add_dv("Beginning Demonstrative")
        project.assign_dv_values_to_dv("Beginning Demonstrative", ["DEM-HA-BEG", "DEM-NO-HA-BEG"])
        project.add_dv("End Demonstratives")
        project.assign_dv_values_to_dv("End Demonstratives", ["DEM-A-END", "DEM-NO-A-END", "DEM-I-END"])
        project.add_dv("here")
        project.assign_dv_values_to_dv("here", ["HNAA", "HNAANA", "HNAAY", "HNAAYA"])
        project.add_dv("Präfix gaʕad")
        project.assign_dv_value_to_dv("Präfix gaʕad", "GA3")
        project.add_dv("Suffix not IA")
        project.assign_dv_values_to_dv("Suffix not IA", ["SUF-A" , "SUF-U"])
        project.add_dv("k/č")
        project.assign_dv_values_to_dv("k/č", ["KC", "CK"])
        project.add_dv("g/q")
        project.assign_dv_values_to_dv("g/q", ["QG", "GQ"])
        project.add_dv("mu")
        project.assign_dv_value_to_dv("mu", "MU")
        project.add_dv("with")
        project.assign_dv_values_to_dv("with", ["WIYYA" , "MA3"])
        

        # Detect the speakers in the file
        project.set_speaker_format("CUSTOM", r"(?P<name>^[A-z0-9?._]+?) ")
        project.detect_speakers()

        # Add some independent variables to the speakers
        project.add_iv("Gender", ["male", "female"])
        project.add_iv("Age", ["old", "young"])
        project.add_iv("pbG Egypt", ["Egypt 5y"])
        project.add_iv("pbG Turkey", ["Turkey 2y"])
        project.add_iv("pbG Diyala", ["Diyala"])
        project.add_iv("pbG Sulaymaniyya", ["Sulaymaniyya"])
        project.add_iv("pbG Baghdad", ["Baghdad"])
        project.add_iv("pbG Emirates", ["Emirates 3y"])
        project.add_iv("pbG only", ["only Baghdad"])
        project.add_iv("pbG Syria", ["Syria 9y", "Syria 8m","Syria 2y","Syria 1y", "Syria 3m"])

        project.assign_iv_value_to_speaker("B", "Gender", "male")
        project.assign_iv_value_to_speaker("B", "Age", "old")
        project.assign_iv_value_to_speaker("B", "pbG Egypt", "Egypt 5y") 

        # Create the main dataset
        project.create_datasets("./tests/test_data/TestOutputArabic", encoding=encoding, separator=";")


    
