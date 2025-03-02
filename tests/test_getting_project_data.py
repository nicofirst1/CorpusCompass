import unittest
from src.model.corpus_compass_model import Project
from src.model.variables_speakers import Variable, VariableValue, Speaker
from src.model.files import File


class GetProjectDataTestCase(unittest.TestCase):
    def test_getting_iv(self):
        """Test if the Independent Variables can be retrieved correctly"""
        project = Project("Testprojekt")
        
        project.add_iv("Age", ["Old", "Young"])
        
        output = project.get_iv_printable()
        expected_output = {'Age': ['Old', 'Young']}
        self.assertEqual(output, expected_output)
    
    def test_getting_dv(self):
        """Test if the Dependent Variables can be retrieved correctly"""
        project = Project("Testprojekt")
        project.add_dv_value("GER_Word", "red")
        project.add_dv_value("ENG_Word", "blue")
        project.add_dv_value("Other_DV_Value", "green") # This value should not be included in the output as it is not assigned to any DV
        project.add_dv("Language")
        project.assign_dv_value_to_dv("Language", "GER_Word")
        project.assign_dv_value_to_dv("Language", "ENG_Word")

        output = project.get_dv_printable()
        expected_output = {'Language': (['GER_Word', 'ENG_Word'], ['red', 'blue'])}
        self.assertEqual(output, expected_output)
    
    def test_getting_speakers(self):
        """Test if the Speakers can be retrieved correctly"""
        project = Project("Testprojekt")
        project.add_iv("Age", ["Old", "Young"])
        project.add_speaker("Speaker A", ["Old"], "red")
        project.add_speaker("Speaker B", ["Young"], "green")
        project.add_speaker("Speaker C")
        
        output = project.get_speakers_printable()
        expected_output = {'Speaker A': ({'Age': 'Old'}, 'red'), 'Speaker B': ({'Age': 'Young'}, 'green'), 'Speaker C': ({}, None)}
        self.assertEqual(output, expected_output)

    def test_getting_dv_values(self):
        """Test if the Dependent Variable Values can be retrieved correctly"""
        project = Project("Testprojekt")
        project.add_dv_value("GER_Word", "red")
        project.add_dv_value("ENG_Word", "blue")
        project.add_dv_value("OTHER", "green")
        project.add_dv("Language", ["GER_Word", "ENG_Word"])
        file = File("TestFile", "utf8", "./virtual_file.txt", 1.0, "Speaker A: Hey, [$how.ENG_Word] are you? Speaker B: I'm fine thanks, what about you? Speaker C: Mir gehts gut, [$danke.GER_Word].")
        project.add_file(file)
        project.add_annotation_format(annotation_str="[$TOKEN.IDENTIFIER]", token="TOKEN", identifier="IDENTIFIER")
        project.detect_annotations()

        output = project.get_dv_values_printable()
        expected_output = {'GER_Word': (1, "Language", 'red'), 'ENG_Word': (1, "Language", 'blue'), 'OTHER': (0, None, 'green')}
        self.assertEqual(output, expected_output)


    
