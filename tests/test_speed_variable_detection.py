import unittest

from model.variables_speaker_detection import (
    SpeakerFormats,
    SpeakerDetector,
    AnnotationDetector,
)
from model.files import File


class SpeedTestCase(unittest.TestCase):
    def test_speed_of_detecting_variables(self):
        """Test if the variable detector can detect variables in files"""
        speaker_detector = SpeakerDetector(SpeakerFormats.STANDARD)
        annotation_detector = AnnotationDetector()

        big_text = (
            "Speaker A: Wow, those new shoes look so [$cool.INFORMAL]. Speaker B: Thank you, I bought them from [$germany.GER]."
            * 1000
        )

        f1 = File("File1", "utf8", "./file1.txt", 1.0, big_text)


if __name__ == "__main__":
    unittest.main()
