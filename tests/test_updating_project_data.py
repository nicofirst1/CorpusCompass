import unittest
from src.model.corpus_compass_model import Project
from src.model.variables_speakers import Variable, VariableValue, Speaker
from src.model.files import File


class UpdateProjectDataTestCase(unittest.TestCase):
    """Test if the Project data can be updated correctly from the frontend input"""
    
    def test_updating_iv(self):
        """Test if the Independent Variables can be updated correctly"""
        project = Project("Testprojekt")
        
        project.add_iv("Age", ["Old", "Young"])

        project.update_iv_from_frontend({"Age": ["Old", "Young", "Middle"], "Language": ["German", "English"]})

        # Check if the IVs have been updated correctly
        self.assertEqual(project.get_iv_printable(), {'Age': ['Old', 'Young', 'Middle'], 'Language': ['German', 'English']})
        
    
    def test_updating_dv(self):
        """Test if the Dependent Variables can be updated correctly"""
        project = Project("Testprojekt")
        project.add_dv_value("GER_Word", "red")
        project.add_dv_value("ENG_Word", "blue")

        project.add_dv("Language")
        project.assign_dv_value_to_dv("Language", "GER_Word")
        project.assign_dv_value_to_dv("Language", "ENG_Word")

        project.update_dv_values_from_frontend({"Informal": (2, "Formality", "red"), "Formal": (1, "Formality", "blue")})

        # Check if the DVs have been updated correctly
        self.assertEqual(project.get_dv_printable(), {'Formality': (['Informal', 'Formal'], ['red', 'blue'])})
    
    def test_updating_speakers(self):
        """Test if the Speakers can be updated correctly"""
        project = Project("Testprojekt")
        project.add_iv("Age", ["Old", "Young"])
        project.add_speaker("Speaker X")

        project.update_speakers_from_frontend({"Speaker A": ({"Age": "Old"}, "red"), "Speaker B": ({"Age": "Young"}, "green")})

        # Check if the Speakers have been updated correctly
        self.assertEqual(project.get_speakers_printable(), {'Speaker A': ({'Age': 'Old'}, 'red'), 'Speaker B': ({'Age': 'Young'}, 'green')})

    def test_updating_annotation_formats(self):
        """Test if the Annotation Formats can be updated correctly"""
        project = Project("Testprojekt")
        
        project.update_annotation_formats_from_frontend({"[$token.identifier]": ["_"]})

        # Check if the Annotation Formats have been updated correctly
        self.assertEqual(project.get_annotation_formats_printable(), {"[$token.identifier]": ["_"]})


    
