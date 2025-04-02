from typing import List, Type


class VariableValue:
    """Class that represents a value of a variable. A variable value can only be assigned to one variable.
    A variable value can have a reference to multiple speakers.
    """

    def __init__(
        self,
        name: str,
        parent: Type["Variable"] = None,
        speakers: list = None,
        color: str = None,
    ) -> None:
        self.parent = parent
        self.name = name
        self.speakers = speakers
        self.color = color
        if not speakers:
            self.speakers = []

    def get_name(self) -> str:
        """
        Returns the name of the variable value
        """
        return self.name

    def has_parent(self) -> bool:
        return self.parent is None

    def set_parent(self, parent: Type["Variable"]) -> None:
        self.parent = parent

    def get_parent(self) -> Type["Variable"]:
        return self.parent

    def has_speaker(self, speaker: Type["Speaker"]) -> bool:
        return speaker in self.speakers

    def get_speakers(self) -> List["Speaker"]:
        return self.speakers

    def add_speaker(self, speaker: Type["Speaker"]) -> bool:
        if self.has_speaker(speaker):
            return False

        self.speakers.append(speaker)
        return True

    def remove_speaker(self, speaker: Type["Speaker"]) -> bool:
        if not self.has_speaker(speaker):
            return False

        self.speakers.remove(speaker)
        return True

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str) -> None:
        self.color = color

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Variable:
    """Class that represents a variable. A variable can have multiple variable values."""

    def __init__(self, name: str, variable_values: List[str] = None) -> None:
        self.name = name

        self.variable_values = {}

        if not variable_values:
            return

        for var_name in variable_values:
            self.variable_values[var_name] = VariableValue(parent=self, name=var_name)

    def get_name(self) -> str:
        return self.name

    def has_variable_value(self, variable_value: str | VariableValue) -> bool:
        """Check if the variable has a specific variable value

        Args:
            variable_value (str | VariableValue): The name of the variable value
            or the variable value object itself that should be checked

        Returns:
            bool: True if the variable has the variable value, False otherwise
        """
        if type(variable_value) == VariableValue:
            variable_value = variable_value.name
        return variable_value in self.variable_values.keys()

    def get_variable_value(self, name: str) -> VariableValue:
        """Get a specific variable value of the variable

        Args:
            name (str): The name of the variable value

        Returns:
            VariableValue: The variable value object if it exists, None otherwise
        """
        if not self.has_variable_value(name):
            return None
        return self.variable_values[name]

    def get_variable_values(self) -> List[VariableValue]:
        """Get all variable values of the variable

        Returns:
            List[VariableValue]: A list of all variable values
        """
        return list(self.variable_values.values())

    def add_variable_value(self, variable_value: str | Type[VariableValue]) -> bool:
        """Add a variable value to the variable

        Args:
            variable_value (str | Type[VariableValue]): The name of the variable value that should be added

        Returns:
            bool: True if the variable value was added successfully, False otherwise
        """
        # Check if the variable value already exists
        if self.has_variable_value(variable_value):
            return False

        # Create a new variable value object
        name = variable_value if type(variable_value) == str else variable_value.name
        variable_value = (
            variable_value
            if type(variable_value) == VariableValue
            else VariableValue(name)
        )
        variable_value.set_parent(self)

        # Add the variable value to the variable
        self.variable_values[name] = variable_value

    def add_variable_values(
        self, variable_values: List[str | Type[VariableValue]]
    ) -> None:
        """Add multiple variable values to the variable

        Args:
            variable_values (List[str | Type[VariableValue]]): A list of variable values that should be added
        """
        for variable_value in variable_values:
            self.add_variable_value(variable_value)

    def remove_variable_value(
        self,
        variable_value: str | Type[VariableValue],
        remove_speaker_reference: bool = True,
    ) -> bool:
        """Remove a variable value from the variable

        Args:
            variable_value (str | Type[VariableValue]): The name of the variable value that should be removed
            remove_speaker_reference (bool, optional): If True, the reference of the variable value will be
                                                       removed from all speakers. Defaults to True.

        Returns:
            bool: True if the variable value was removed successfully, False otherwise
        """

        # Check if the variable value exists
        if not self.has_variable_value(variable_value):
            return False

        if type(variable_value) == VariableValue:
            variable_value = variable_value.name

        # Remove the reference to the variable value from all speakers
        if remove_speaker_reference:
            speakers = self.variable_values[variable_value].get_speakers().copy()
            for speaker in speakers:
                speaker.remove_iv_value(variable_value)

        # Remove the variable value from the variable
        del self.variable_values[variable_value]
        return True

    def serialize(self) -> str:
        """Serialize the variable

        Returns:
            str: The serialized variable
        """
        return f"'{self.name}': {list(self.variable_values.keys())}"

    @staticmethod
    def to_dict(variables: List["Variable"]) -> dict:
        """Represents the given variables as a dictionary

        Args:
            variables (List[Variable]): The variables that should be represented as a dictionary

        Returns:
            dict: The dictionary representation of the variables
        """
        res = {}
        variable_list = []

        for variable in variables:
            variable_data = {}
            variable_data["Name"] = variable.get_name()
            variable_value_list = []
            for variable_value in variable.get_variable_values():
                variable_value_data = {}
                variable_value_data["Name"] = variable_value.get_name()
                variable_value_data["Color"] = variable_value.get_color()
                variable_value_data["Speakers"] = [
                    str(speaker) for speaker in variable_value.get_speakers()
                ]
                variable_value_list.append(variable_value_data)
            variable_data["VariableValues"] = variable_value_list
            variable_list.append(variable_data)

        res["Variables"] = variable_list

        return res

    def __repr__(self) -> str:
        return self.name


class Speaker:
    """Class that represents a speaker. A speaker can have multiple independent variable values
    assigned to him.
    """

    def __init__(
        self, name: str, iv_values: List[VariableValue] = None, color: str = None
    ) -> None:
        self.name = name
        self.iv_values = iv_values
        self.color = color

        if not iv_values:
            self.iv_values = []

        for iv_value in self.iv_values:
            iv_value.add_speaker(self)

    def has_iv_value(self, iv_value: str | VariableValue) -> bool:
        """Check if the speaker has a specific independent variable value assigned

        Args:
            iv_value (str | VariableValue): The name of the independent variable value or the
            independent variable value object that should be checked

        Returns:
            bool: True if the speaker has the independent variable value, False otherwise
        """
        if type(iv_value) == VariableValue:
            return iv_value in self.iv_values

        for iv_value_speaker in self.iv_values:
            if iv_value_speaker.name == iv_value:
                return True
        return False

    def add_iv_value(self, iv_value: VariableValue) -> bool:
        """Assign an independent variable value to the speaker. If the independent variable value
        is already assigned to the speaker, the method will return False.

        Args:
            iv_value (VariableValue): The independent variable value that should be assigned

        Returns:
            bool: True if the independent variable value was assigned successfully, False otherwise
        """
        if iv_value in self.iv_values:
            return False

        self.iv_values.append(iv_value)
        iv_value.add_speaker(self)
        return True

    def remove_iv_value(self, iv_value: VariableValue | str) -> bool:
        """Remove an independent variable value from the speaker. If the independent variable value
        is not assigned to the speaker, the method will return False.

        Args:
            iv_value (VariableValue | str): The independent variable value that should be removed

        Returns:
            bool: True if the independent variable value was removed successfully, False otherwise
        """
        # Check if the independent variable value exists
        if not self.has_iv_value(iv_value):
            return False

        # Case: iv_value is a VariableValue object
        if type(iv_value) == VariableValue:
            self.iv_values.remove(iv_value)
            iv_value.remove_speaker(self)
            return True

        # Case: iv_value is a string
        for i in range(len(self.iv_values)):
            iv_name = self.iv_values[i].name
            if iv_name == iv_value:
                temp_value = self.iv_values.pop(i)
                temp_value.remove_speaker(self)
                return True

    def get_iv_values(self) -> List[VariableValue]:
        return self.iv_values

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str) -> None:
        self.color = color

    def __repr__(self) -> str:
        return self.name

    @staticmethod
    def to_dict(speakers: list) -> dict:
        """Represents the given speakers as a dictionary

        Args:
            speakers (list): The speakers that should be represented as a dictionary

        Returns:
            dict: The dictionary representation of the speakers
        """
        res = {}
        speakers_list = []

        for speaker in speakers:
            speaker_data = {}
            iv_data = {}
            for iv_value in speaker.get_iv_values():
                iv_data[str(iv_value.get_parent())] = str(iv_value)

            speaker_data["Name"] = speaker.get_name()
            speaker_data["Color"] = speaker.get_color()
            speaker_data["Variables"] = iv_data
            speakers_list.append(speaker_data)

        res["Speakers"] = speakers_list
        return res
