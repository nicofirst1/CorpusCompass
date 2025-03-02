import unittest

from src.model.variables_speaker_detection import (
    SpeakerFormats,
    SpeakerDetector,
    AnnotationDetector,
)
from src.model.files import File


class SpeakerDetectorTestCase(unittest.TestCase):
    def test_finding_speakers_in_files(self):
        """Test if the speaker detector can find speakers in files"""
        speaker_detector = SpeakerDetector(SpeakerFormats.STANDARD)
        f1 = File(
            "File1",
            "utf8",
            "./file1.txt",
            1.0,
            "Speaker A: Hey, how are you? Speaker B: I'm fine thanks, what about you? Speaker C: I'm good, thank you.",
        )
        f2 = File(
            "File2",
            "utf8",
            "./file2.txt",
            2.0,
            "Speaker C: Have you already learned for the exam next week? Speaker D: Nah, I will rely on my luck.",
        )

        detected_speakers = speaker_detector.detect_speakers([f1, f2])

        self.assertEqual(
            list(detected_speakers["speaker_name"].unique()),
            ["Speaker A", "Speaker B", "Speaker C", "Speaker D"],
        )


class AnnotationDetectorTestCase(unittest.TestCase):
    def test_creating_re_from_str(self):
        """Test if the annotation detector can create a correct regular expression"""
        annotation_detector = AnnotationDetector()

        # Check if the detector generates a correct re from the following string:
        annotation_format_str = "[$TOKEN.IDENTIFIER]"
        annotation_detector.add_annotation_format_token_identifier(
            annotation_str=annotation_format_str, token=(2, 6), identifier=(8, 17)
        )
        annotation_re, _ = annotation_detector.get_annotation_format(
            annotation_format_str
        )
        self.assertEqual(annotation_re, r"\[\$(?P<token>\w+)\.(?P<identifier>\w+)\]")

        # Check if identifier before token can be handled correctly, also use different formulation for token and identifier and a different annotation format
        annotation_format_str = "{id_token}"
        annotation_detector.add_annotation_format_token_identifier(
            annotation_str=annotation_format_str, token=(4, 8), identifier=(1, 2)
        )
        annotation_re, _ = annotation_detector.get_annotation_format(
            annotation_format_str
        )
        self.assertEqual(annotation_re, r"\{(?P<identifier>\w+)_(?P<token>\w+)\}")

        # Check if multiple identifiers are handled correctly
        annotation_format_str = "TOKEN_IDENTIFIER"
        multiple_identifier_separator = "$"
        annotation_detector.add_annotation_format_token_identifier(
            annotation_str=annotation_format_str,
            token=(0, 4),
            identifier=(6, 15),
            multiple_identifier_separator=multiple_identifier_separator,
        )
        annotation_re, _ = annotation_detector.get_annotation_format(
            annotation_format_str
        )
        self.assertEqual(annotation_re, r"(?P<token>\w+)_(?P<identifier>\w+(\$\w+)*)")

    def test_finding_annotations_in_files(self):
        """Test if the annotation detector can find annotations in files and
        extract the token and identifier correctly
        """
        annotation_detector = AnnotationDetector()
        annotation_detector.add_annotation_format_token_identifier(
            annotation_str="[$TOKEN.IDENTIFIER]", token=(2, 6), identifier=(8, 17)
        )

        f1 = File(
            "File1",
            "utf8",
            "./file1.txt",
            1.0,
            "Speaker A: Wow, those new shoes look so [$cool.INFORMAL]. Speaker B: Thank you, I bought them from [$germany.GER].",
        )
        f2 = File(
            "File2",
            "utf8",
            "./file2.txt",
            2.0,
            "Speaker C: I have a lot of [$work.JOB] to do.",
        )

        detected_annotations = annotation_detector.detect_annotations([f1, f2])

        found_tokens = detected_annotations["token"].tolist()
        self.assertEqual(found_tokens, ["cool", "germany", "work"])

        found_identifiers = detected_annotations["identifier"].explode().tolist()
        self.assertEqual(found_identifiers, ["INFORMAL", "GER", "JOB"])

    def test_finding_multiple_identifiers(self):
        """Test if the annotation detector can find multiple identifiers in an annotation"""
        annotation_detector = AnnotationDetector()
        annotation_detector.add_annotation_format_token_identifier(
            annotation_str="[$TOKEN.IDENTIFIER]",
            token=(2, 6),
            identifier=(8, 17),
            multiple_identifier_separator="_",
        )

        f1 = File(
            "File1",
            "utf8",
            "./file1.txt",
            1.0,
            "Speaker A: Winter is [$coming.IDENTIFIER1_IDENTIFIER2]",
        )
        f2 = File(
            "File2",
            "utf8",
            "./file2.txt",
            2.0,
            "Speaker B: I have a lot of [$work.IDENTIFIER1_IDENTIFIER2_IDENTIFIER3_IDENTIFIER4] to do.",
        )

        detected_annotations = annotation_detector.detect_annotations([f1, f2])
        self.assertEqual(
            detected_annotations.loc[0, "identifier"], ["IDENTIFIER1", "IDENTIFIER2"]
        )
        self.assertEqual(
            detected_annotations.loc[1, "identifier"],
            ["IDENTIFIER1", "IDENTIFIER2", "IDENTIFIER3", "IDENTIFIER4"],
        )

    def test_finding_annotations_with_identifier_before_token(self):
        """Test if the annotation detector can find multiple identifiers in an annotation"""
        annotation_detector = AnnotationDetector()
        annotation_detector.add_annotation_format_token_identifier(
            annotation_str="[$IDENTIFIER.TOKEN]",
            token="TOKEN",
            identifier="IDENTIFIER",
            multiple_identifier_separator=".",
        )

        file = File(
            "File1",
            "utf8",
            "./file1.txt",
            1.0,
            "Speaker A: Winter is [$IDENTIFIER1.IDENTIFIER2.coming]",
        )

        detected_annotations = annotation_detector.detect_annotations([file])
        self.assertEqual(
            detected_annotations.loc[0, "identifier"], ["IDENTIFIER1", "IDENTIFIER2"]
        )


if __name__ == "__main__":
    unittest.main()
