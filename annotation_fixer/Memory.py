import json
import os
from typing import Dict


class SavingDict(dict):

    def __init__(self, save_fn, attr, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._save_fn = save_fn
        self._attr = attr


    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save_fn(self._attr)

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save_fn(self._attr)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._save_fn(self._attr)

    def pop(self, *args, **kwargs):
        super().pop(*args, **kwargs)
        self._save_fn(self._attr)

    def popitem(self, *args, **kwargs):
        super().popitem(*args, **kwargs)
        self._save_fn(self._attr)


class Memory:
    """
    Class to store the memory of the annotation fixer
    """

    def __init__(self):
        self.dir = ".annotation_fixer"
        # create dir if not exists
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

        # create the files
        self.file_lfp = os.path.join(self.dir, "lfp.json")
        self.file_settings = os.path.join(self.dir, "settings.json")

        # create the attributes
        self._lfp = SavingDict(self.save_memory, attr="file_lfp")
        self._settings = SavingDict(self.save_memory, attr="file_settings")

        # load the memory
        self.load_memory()

    def load_memory(self):
        """
        Load the memory from the files
        """
        # for all the attributes that end with _paths
        for attr in [a for a in dir(self) if a.startswith("file_")]:

            attr_value = getattr(self, attr)
            # create files if not exists
            if not os.path.exists(attr_value):
                with open(attr_value, "w") as f:
                    json.dump({}, f)

            # get the hidden attribute name without the file_ prefix

            hid_attr = attr.replace("file_", "")

            # load the paths from the file
            with open(attr_value, "r") as f:
                setattr(self, hid_attr, json.load(f))

    def save_memory(self, attr=None):
        """
        Save the memory to the files
        """

        if attr is None:
            attrs = [a for a in dir(self) if a.startswith("file_")]
        else:
            attrs = [attr]

        # for all the attributes that end with _paths
        for attr in attrs:
            attr_value = getattr(self, attr)
            # get the hidden attribute name without the file_ prefix
            hid_attr = attr.replace("file_", "_")

            # save the paths to the file
            with open(attr_value, "w") as f:
                json.dump(getattr(self, hid_attr), f)

    @property
    def lfp(self):
        return self._lfp

    @lfp.setter
    def lfp(self, value: Dict[str, str]):

        self._lfp.update(value)
        self.save_memory("file_lfp")
