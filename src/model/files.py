from PySide6.QtCore import Signal, QThread
from src.utils.file_utils import decode_txt_file
from typing import List
import os


class File():
    """Class that represents a file with the following attributes:
    - name: The name of the file, including the file extension
    - encoding: The encoding of the file
    - content: The content of the file as a string
    - path: The path of the file excluding the filename
    - version: The version of the file, which is the time of the last modification
    - number_of_chars: The number of characters in the file
    """
    def __init__(self, file_name: str, encoding: str, file_path: str, file_version: float = None, file_content: str = None) -> None:
        self.name = file_name
        self.encoding = encoding
        self.content = file_content
        self.path = os.path.abspath(file_path)
        self.version = file_version
        if not file_version:
            self.version = File.get_version_from_filepath(self.path)
        if file_content:
            self.number_of_chars = len(self.content)
        else:
            self.number_of_chars = 0
    
    def get_file_name(self, include_extension: bool = True) -> str:
        """Returns the name of the file.

        Args:
            include_extension (bool, optional): If True, the file extension is included in the name. Defaults to True.

        Returns:
            str: The name of the file
        """
        if include_extension:
            return self.name
        return os.path.splitext(self.name)[0]
    
    def get_file_content(self) -> str | None:
        """Returns the content of the file.

        Returns:
            str: The content of the file
        """
        return self.content


    def get_file_version(self) -> float:
        """Returns the version of the file.

        Returns:
            float: The version of the file
        """
        return self.version
    
    def get_file_path(self) -> str:
        """Returns the path of the file.

        Returns:
            str: The path of the file
        """
        return self.path

    def was_file_modified(self) -> bool:
        """Returns True if the file was modified since the last time the version was checked.

        Returns:
            bool: True if the file was modified, False otherwise
        """
        return self.version != File.get_version_from_filepath(self.path)
    
    def was_file_moved(self) -> bool:
        """Returns True if the file is not found under the given path.

        Returns:
            bool: True if the file cannot be found under the given path, False otherwise
        """
        return not os.path.isfile(self.path)
    
    def update_file_content(self, content: str) -> None:
        """Updates the content of the file and the version.

        Args:
            content (str): The new content of the file
            file_version (float): The new version of the file
        """
        self.content = content
        self.version = File.get_version_from_filepath(self.path)
        self.number_of_chars = len(self.content)

    def save_as_txt(self) -> None:
        """Saves the file as a .txt file. Is mainly used for testing purposes.
        """
        with open(self.path, 'w', encoding=self.encoding) as outfile:
            outfile.write(self.content)

    def __repr__(self) -> str:
        return self.name

    @staticmethod
    def to_dict(files: list) -> dict:
        """Returns a dictionary representation of the files in the files list.

        Args:
            files (list): A list of File objects

        Returns:
            dict: A dictionary representation of the files in the files list
        """
        file_list = []
        res = {"Files": file_list}
        for file in files:
            file_data = {}
            file_data[file.name] = {
                "encoding": file.encoding,
                "path": file.path,
                "version": file.version,
                "number_of_chars": file.number_of_chars
            }
            file_list.append(file_data)
        return res

    @staticmethod
    def get_version_from_filepath(file_path: str) -> float:
        """Returns the version of the file under the given file_path.

        Args:
            file_path (str): The path of the file

        Returns:
            float: The version of the file
        """
        return os.path.getmtime(file_path)



class FileLoader(QThread):
    """Class that loads a file in a separate thread. The loaded file can be received
    synchronously or asynchronously. If the file is received asynchronously, the signals
    loading_file_finished and loading_file_failed are emitted. If the file is received
    synchronously, the method get_result can be called to get the loaded file.
    """
    loading_file_finished = Signal(File)
    loading_file_failed = Signal(Exception)

    def __init__(self, file_paths: List[str] = None, files_to_reload: List[File] = None, use_signal: bool = True) -> List | None:
        super().__init__()
        self.file_paths = file_paths
        self.use_signal = use_signal
        self.files_to_reload = files_to_reload
    
    def run(self) -> List | None:
        if self.file_paths:
            return self.load_files_from_paths()
        elif self.files_to_reload:
            return self.reload_files()
    
    def reload_files(self) -> None | List[File]:
        """Reloads the files in the files_to_reload list. If the file is loaded successfully
        and the use_signal attribute is set to True, the signal loading_file_finished 
        is emitted. If the file could not be loaded, the signal loading_file_failed is emitted.
        """
        results = []
        for file in self.files_to_reload:
            file_path = file.get_file_path()

            # Check if the file exists
            if not os.path.exists(file_path):
                self.loading_file_failed.emit(FileNotFoundError(f'Unable to find a file under the given path: "{file_path}"'))
                return
            
            file_extension = os.path.splitext(file_path)[1]
            file_encoding = file.encoding

            # Check if the file extension is supported
            if file_extension == ".txt":
                # Load the file
                file_text, encoding, error = decode_txt_file(file_path, file_encoding)
            else:
                self.loading_file_failed.emit(NotImplementedError(f'The following File-extension is not supported for loading in: "{file_extension}"'))
                return

            file.update_file_content(file_text)

            # Emit the signal
            if self.use_signal:
                self.loading_file_finished.emit(file)
            else:
                results.append(file)
        
        if not self.use_signal:
            return results

    def load_files_from_paths(self) -> List | None:
        """Loads the files in the file_paths list. If the file is loaded successfully
        and the use_signal attribute is set to True, the signal loading_file_finished 
        is emitted. If the file could not be loaded, the signal loading_file_failed is emitted.
        """
        # Will only be used to store the result if the use_signal attribute is set to False
        results = []

        # Iterate over all file paths
        for file_path in self.file_paths:
            # Check if the file exists
            if not os.path.exists(file_path):
                self.loading_file_failed.emit(FileNotFoundError(f'Unable to find a file under the given path: "{file_path}"'))
                return
            
            file_path_no_ext, file_extension = os.path.splitext(file_path)
            file_name = os.path.basename(file_path_no_ext)

            # Check if the file extension is supported
            if file_extension == ".txt":
                # Load the file
                file_text, encoding, error = decode_txt_file(file_path)
            else:
                self.loading_file_failed.emit(NotImplementedError(f'The following File-extension is not supported for loading in: "{file_extension}"'))
                return

            file = File(file_name=file_name + file_extension, 
                        encoding=encoding, 
                        file_content=file_text, 
                        file_path=file_path)

            # Emit the signal or set the result
            if self.use_signal:
                self.loading_file_finished.emit(file)
            else:
                results.append(file)
        
        if not self.use_signal:
            return results
