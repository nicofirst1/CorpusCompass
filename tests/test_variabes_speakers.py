import unittest

from src.model.variables_speakers import Speaker, Variable, VariableValue


class VariableTestCase(unittest.TestCase):
    def test_finding_iv_values(self):
        iv = Variable(name="Age", variable_values=["Young", "Old"])
        self.assertTrue(iv.has_variable_value("Young"))
        self.assertFalse(iv.has_variable_value("Student"))

    def test_adding_a_iv_value(self):
        iv = Variable(name="Age", variable_values=["Young"])

        # Method 1:
        iv.add_variable_value("Old")
        self.assertTrue(iv.has_variable_value("Old"))

        # Method 2:
        iv_value = VariableValue("Child")
        iv.add_variable_value(iv_value)

        self.assertTrue(iv.has_variable_value("Child"))

        # Check for duplicates:
        result = iv.add_variable_value("Old")
        self.assertFalse(result)

    def test_removing_iv_value(self):
        iv = Variable(name="Age", variable_values=["Young", "Old", "UnwantedVar1"])

        success = iv.remove_variable_value("UnwantedVar1")

        # Check if deletion was successfull
        self.assertTrue(success)

        # Check if the Variable is no longer available
        self.assertFalse(iv.has_variable_value("UnwantedVar1"))

        success = iv.remove_variable_value("NonExistingVar")

        # This deletion should fail, since the variable never existed
        self.assertFalse(success)


class SpeakerTestCase(unittest.TestCase):
    def test_assigning_iv_values_to_speaker(self):
        iv = Variable(name="Popularity", variable_values=["Cool", "Uncool"])
        speaker = Speaker("A")

        # Currently the speaker should have zero iv-values assigned
        self.assertTrue(len(speaker.get_iv_values()) == 0)
        self.assertFalse(speaker.has_iv_value("Cool"))

        speaker.add_iv_value(iv.get_variable_value("Cool"))

        # Now try to look for the added iv-value
        self.assertTrue(len(speaker.get_iv_values()) == 1)
        self.assertTrue(speaker.has_iv_value("Cool"))

    def test_removing_iv_values_from_speaker(self):
        iv = Variable(name="Age", variable_values=["Young", "Old"])

        # Speaker1, speaker2 and speaker 3 get the iv-value "Old" assigned to them
        speaker1 = Speaker("A")
        speaker1.add_iv_value(iv.get_variable_value("Old"))

        speaker2 = Speaker("B")
        speaker2.add_iv_value(iv.get_variable_value("Old"))

        speaker3 = Speaker("C")
        speaker3.add_iv_value(iv.get_variable_value("Old"))

        speaker1.remove_iv_value("Old")

        # Now the iv-value should be removed from speaker1
        self.assertFalse(speaker1.has_iv_value("Old"))

        # But speaker2 should still have the iv-value
        self.assertTrue(speaker2.has_iv_value("Old"))

        # However, if the iv-value "Old" is removed from the iv, all speakers containing
        # the iv value should delete the reference to it:
        iv.remove_variable_value("Old")
        self.assertFalse(speaker2.has_iv_value("Old"))
        self.assertFalse(speaker3.has_iv_value("Old"))
