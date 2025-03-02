from src.model.files import File, FileLoader
import time
import os
import unittest


class FileTestCase(unittest.TestCase):
    def test_creating_a_file(self):
        """Test if a file can be created correctly, will be used for further tests"""
        file_name = "test_file.txt"
        file_path = os.path.join("./tests/test_data", file_name)
        file_content = "This is a Test file"
        encoding = "utf-8"

        with open(file_path, "w", encoding=encoding) as outfile:
            outfile.write(file_content)

        file = File(
            file_name=file_name,
            encoding=encoding,
            file_path=file_path,
            file_content=file_content,
        )
        self.assertEqual(type(file.version), float)

    def test_loading_file(self):
        """Test if a file can be loaded correctly"""
        file_name = "test_file.txt"
        file_path = os.path.abspath(os.path.join("./tests/test_data", file_name))

        file_loader = FileLoader(file_paths=[file_path], use_signal=False)
        files = file_loader.run()
        file = files[0]
        self.assertEqual(file.name, file_name)
        self.assertEqual(file.encoding, "utf-8")
        self.assertEqual(file.content, "This is a Test file\n")
        self.assertEqual(file.path, file_path)

    def test_loading_file_with_wrong_path(self):
        """Test if a file loader raises a FileNotFoundError if the path is wrong"""
        file_loader = FileLoader(
            ["./tests/test_data/non_existing_file.txt"], use_signal=False
        )

        error_received = [False]

        def error_occured_received(ex: Exception):
            error_received[0] = True
            self.assertEqual(type(ex), FileNotFoundError)

        file_loader.loading_file_failed.connect(error_occured_received)
        file_loader.start()
        file_loader.wait()

    def test_file_version(self):
        """Test if the file version can be correctly used to determine if a file has changed"""

        # Create a file
        file_name = "modified_file.txt"
        file_path = os.path.join("./tests/test_data", file_name)
        file_content = "This content will be modified later on!"
        encoding = "utf-8"

        with open(file_path, "w", encoding=encoding) as outfile:
            outfile.write(file_content)

        file_loader = FileLoader(file_paths=[file_path], use_signal=False)
        files = file_loader.run()
        file = files[0]

        # Modify the file

        # We need to wait at least one second after the creation of the file
        # before modifying it. This is because the file version is based on the
        # last modification time in seconds. If we modify the file too quickly
        # after creating it, the version will not change.
        time.sleep(1)

        with open(file_path, "w", encoding=encoding) as outfile:
            outfile.write("This content has been modified!")

        file_loader = FileLoader([file_path], use_signal=False)
        files = file_loader.run()
        modified_file = files[0]

        # Check if the version of the file has changed
        self.assertNotEqual(file.version, modified_file.version)

        # Loading the file again should not change the version
        file_loader = FileLoader([file_path], use_signal=False)
        files = file_loader.run()
        file = files[0]

        self.assertEqual(file.version, modified_file.version)
