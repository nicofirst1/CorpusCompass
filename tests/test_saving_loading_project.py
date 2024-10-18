import unittest

from src.model.files import File
from src.model.corpus_compass_model import Project

class SavingLoadingTestCase(unittest.TestCase):
    """Test if a project can be saved and loaded correctly"""

    def test_saving_a_project(self):
        """Test if a project can be saved correctly
        """
        project = Project("TestProject", "This is a test project used for testing the saving and loading of projects.")

        # Add some files to the project
        f1 = File("File1", "utf8", "./tests/test_data/TestProject/file1.txt", 1.0, "Speaker A: Hey, how are you? Speaker B: I'm fine thanks, what about you? Speaker C: I'm good, thank [$you.VAL1].")
        f2 = File("File2", "utf8", "./tests/test_data/TestProject/file2.txt", 2.0, "Speaker C: Have you already learned for the exam next week? Speaker D: [$Nah.VAL2], I will rely on my [$luck.VAL3].")
        project.add_file(f1)
        project.add_file(f2)
        # Also save the files so that they can be used for loading the project
        f1.save_as_txt()
        f2.save_as_txt()

        # Add a Dependent Variable to the project by detecting the variables in the files
        project.add_annotation_format(annotation_str="[$TOKEN.IDENTIFIER]",
                                      token="TOKEN",
                                      identifier="IDENTIFIER")
        project.add_annotation_format(annotation_str="{!TOKEN:IDENTIFIER!}",
                                      token="TOKEN",
                                      identifier="IDENTIFIER",
                                      multiple_identifier_separator="_")
        project.detect_annotations()
        project.add_dv("DV1")
        project.assign_dv_value_to_dv("DV1", "VAL1")
        project.assign_dv_value_to_dv("DV1", "VAL2")

        project.set_dv_value_color("VAL1", "red")

        # Add a Independent Variable to the project
        project.add_iv("Age", ["Young", "Old"])

        # Add Speakers to the project
        project.add_speaker("Speaker A", )
        project.add_speaker("Speaker B", ["Old"])

        # Detect speakers in the files
        project.detect_speakers()

        # Save the project
        project.save_project("./tests/test_data")
    
    def test_loading_a_project(self):
        """Test if a project can be loaded correctly
        """
        project = Project.load_project("./tests/test_data/TestProject", is_synchronous=True)

        self.assertEqual(project.get_name(), "TestProject")
        self.assertEqual(project.get_speaker_format(), "STANDARD")
        self.assertEqual(project.get_description(), "This is a test project used for testing the saving and loading of projects.")
        self.assertEqual(len(project.files), 2)
        self.assertEqual(len(project.dependent_variable_values), 3)
        self.assertEqual(len(project.independent_variables), 1)
        self.assertEqual(len(project.speakers), 4)

        # Check if the independent variable is loaded correctly
        iv = project.get_iv("Age")
        self.assertEqual(iv.name, "Age")
        self.assertTrue(iv.has_variable_value("Old"))
        self.assertTrue(iv.has_variable_value("Young"))
        iv_value = iv.get_variable_value("Old")

        # Check if the speakers are loaded correctly
        self.assertTrue(project.exists_speaker("Speaker B"))
        s1 = project.get_speaker("Speaker B")
        self.assertTrue(s1.has_iv_value("Old"))
        self.assertTrue(iv_value.has_speaker(s1))

        # Check if the dependent variables are loaded correctly
        dv1 = project.get_dv("DV1")
        self.assertEqual(dv1.name, "DV1")
        self.assertTrue(dv1.has_variable_value("VAL1"))
        self.assertTrue(dv1.has_variable_value("VAL2"))
        self.assertFalse(dv1.has_variable_value("VAL3"))
        self.assertTrue(project.exists_dv_value("VAL3"))
        dv1_value = dv1.get_variable_value("VAL1")
        self.assertEqual(dv1_value.color, "red")

        # Check if the files are loaded correctly
        f1 = project.files[0]
        self.assertEqual(f1.name, "File1")
        self.assertEqual(f1.encoding, "utf8")
        self.assertEqual(f1.content, "Speaker A: Hey, how are you? Speaker B: I'm fine thanks, what about you? Speaker C: I'm good, thank [$you.VAL1].\n")

        f2 = project.files[1]
        self.assertEqual(f2.name, "File2")
        self.assertEqual(f2.encoding, "utf8")
        self.assertEqual(f2.content, "Speaker C: Have you already learned for the exam next week? Speaker D: [$Nah.VAL2], I will rely on my [$luck.VAL3].\n")

        # Check if the dependent variable values are loaded correctly
        dv1 = project.get_dv_value("VAL1")
        self.assertEqual(dv1.name, "VAL1")
        

if __name__ == "__main__":
    unittest.main()