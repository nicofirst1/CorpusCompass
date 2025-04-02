import unittest
from model.corpus_compass_model import Project


class ProjectTestCase(unittest.TestCase):
    def test_adding_ivs_and_iv_values(self):
        project = Project("Testprojekt")

        project.add_iv("Age", ["Old", "Young"])

        self.assertTrue("Age" in project.independent_variables)

        iv1 = project.independent_variables["Age"]

        self.assertTrue(iv1.has_variable_value("Old"))
        self.assertTrue(iv1.has_variable_value("Young"))
        self.assertFalse(iv1.has_variable_value("Cool"))

        project.add_iv_value_to_iv("Age", "Cool")
        self.assertTrue(iv1.has_variable_value("Cool"))

        error_received = [False]

        def error_occured_received(message: str):
            error_received[0] = True
            self.assertEqual(
                message,
                'The Independent Variable with the name "Non-existing Variable" was not found!',
            )

        project.error_occurred_signal.connect(error_occured_received)
        project.add_iv_value_to_iv("Non-existing Variable", "Cool")
        self.assertTrue(error_received[0])

    # def test_saving_ivs_as_json(self):
    #    project = Project("Testprojekt")
    #
    #    project.add_iv("Age", ["Old", "Young"])
    #    project.add_iv("Herritage", ["GER", "ENG", "FR"])
    #
    #    project.save_ivs_as_json("./iv_test.json")

    def test_adding_dv_values(self):
        project = Project("Testprojekt")

        # First, the dv values would be extracted from the corpus and then
        # added to the project
        dv_values = ["GER_Word", "ENG_Word", "FR_Word", "INFORMAL", "FORMAL"]

        for dv_value in dv_values:
            project.add_dv_value(dv_value)

        self.assertEqual(len(project.dependent_variable_values), 5)

        self.assertTrue(project.exists_dv_value("GER_Word"))

        self.assertFalse(project.exists_dv_value("Non-existing Value"))

        # Assigning an dv value with a name that already exists should not be possible
        error_received = [False]

        def error_occured_received(message: str):
            error_received[0] = True
            self.assertEqual(
                message, 'The dependent variable value "GER_Word" already exists!'
            )

        project.error_occurred_signal.connect(error_occured_received)
        project.add_dv_value("GER_Word")

        self.assertTrue(error_received[0])

    def test_assigning_dv_values_to_dv(self):
        project = Project("Testprojekt")

        dv_values = ["GER_Word", "ENG_Word", "FR_Word"]

        for dv_value in dv_values:
            project.add_dv_value(dv_value)

        project.add_dv("Language")
        project.assign_dv_value_to_dv("Language", "GER_Word")
        project.assign_dv_value_to_dv("Language", "ENG_Word")
        project.assign_dv_value_to_dv("Language", "FR_Word")

        self.assertEqual(
            len(project.dependent_variables["Language"].get_variable_values()), 3
        )

        project.add_dv("Formality", ["INFORMAL", "FORMAL"])
        self.assertEqual(
            len(project.dependent_variables["Formality"].get_variable_values()), 2
        )

        # Assigning a dv value that does not exist should not be possible
        error_received = [False]

        def error_occured_received(message: str):
            error_received[0] = True
            self.assertEqual(
                message,
                'The dependent variable value "Non-existing Value" does not exist!',
            )

        project.error_occurred_signal.connect(error_occured_received)
        project.assign_dv_value_to_dv("Language", "Non-existing Value")

        self.assertTrue(error_received[0])


if __name__ == "__main__":
    unittest.main()
