# -*- coding: utf-8 -*-
"""
project.py
Author: Gilson, K.
"""

from typing import Any, List, Optional

from .mixin import JSONableMixin


class Project(JSONableMixin):
    """Project: inherit from 'JSONableMixin'.

    Attributes:
        name (str, optional): name of the project. Defaults to None.
        redacted (str, optional): confidential proxy name of the project. Defaults to None.
        position (str, optional): title of the position within the project. Defaults to None.
        start (int, optional): start date of the project under YYYYMM format. Defaults to None.
        end (int, optional): end date of the project under YYYYMM format. Defaults to None.
        description (List[str], optional): list of paragraphs of the description. Defaults to None.
        activities (List[str], optional): list of the activities. Defaults to None.
        confidential (bool, optional): whether to treat the project as confidential or not. Defaults to True.
    """

    def __init__(
        self,
        name: Optional[str] = None,
        redacted: Optional[str] = None,
        position: Optional[str] = None,
        start: Optional[int] = None,
        end: Optional[int] = None,
        description: Optional[List[str]] = None,
        activities: Optional[List[str]] = None,
        confidential: Optional[bool] = True,
    ) -> None:
        """Initialize the Project class instance.

        Args:
            name (str, optional): name of the project. Defaults to None.
            redacted (str, optional): confidential proxy name of the project. Defaults to None.
            position (str, optional): title of the position within the project. Defaults to None.
            start (int, optional): start date of the project under YYYYMM format. Defaults to None.
            end (int, optional): end date of the project under YYYYMM format. Defaults to None.
            description (List[str], optional): list of paragraphs of the description. Defaults to None.
            activities (List[str], optional): list of the activities. Defaults to None.
            confidential (bool, optional): whether to treat the project as confidential or not. Defaults to True.
        """
        self.name = name
        self.redacted = redacted
        self.position = position
        self.start = start
        self.end = end
        self.description = description
        self.activities = activities
        self.confidential = confidential

    def __setattr__(self, name: str, value: Any) -> None:
        """Validate the attributes of the Project class.

        Args:
            name (str): the name of the attribute.
            value (Any): the value of the attribute.

        Raises:
            TypeError: if 'name', 'redacted', or 'position' are not str.
            TypeError: if 'start' or 'end' are not an int.
            AttributeError: if 'start' or 'end' have and incorrect length.
            TypeError: if 'description' or 'activities' are not a list.
        """
        if value is not None:
            if name in ["name", "redacted", "position"] and not isinstance(value, str):
                raise TypeError(f"'{name}' expect a str.")
            elif name in ["start", "end"]:
                if not isinstance(value, int):
                    raise TypeError(f"'{name}' expect an int.")
                elif len(str(value)) != 6:
                    raise AttributeError(
                        f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format."
                    )
            elif name in ["description", "activities"] and not isinstance(value, list):
                raise TypeError(f"'{name}' expect a list.")
            elif name == "confidential" and not isinstance(value, bool):
                raise TypeError(f"'{name}' expect a bool.")

        self.__dict__[name] = value

    # Description
    def add_description(self, new_description: str) -> "Project":
        """Add a paragraph to the description attribute.

        Args:
            new_description (str): the paragraph to add.

        Raises:
            TypeError: if new_description is not a str.

        Returns:
            Project: the class instance itself.
        """
        if not isinstance(new_description, str):
            raise TypeError("'new_description' expect a str.")

        if self.description is None:
            self.description = []
        self.description.append(new_description)
        return self

    def remove_description(self, old_description: str) -> "Project":
        """Remove a paragraph from the description attribute.

        Args:
            old_description (str): the paragraph to remove.

        Raises:
            TypeError: if old_description is not a str.

        Returns:
            Project: the class instance itself.
        """
        if not isinstance(old_description, str):
            raise TypeError("'old_description' expect a str.")

        self.description.remove(old_description)
        return self

    def reorder_description(self, order: list) -> "Project":
        """Reorder the description attribute.

        Args:
            order (list): the new order of the description attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Project: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.description = [self.description[i] for i in order]
        return self

    # Activities
    def add_activity(self, new_activity: str) -> "Project":
        """Add an activity to the activities attribute.

        Args:
            new_activity (str): the activity to add.

        Raises:
            TypeError: if new_activity is not a str.

        Returns:
            Project: the class instance itself.
        """
        if not isinstance(new_activity, str):
            raise TypeError("'new_activity' expect a str.")

        if self.activities is None:
            self.activities = []
        self.activities.append(new_activity)
        return self

    def remove_activity(self, old_activity: str) -> "Project":
        """Remove an activity from the activities attribute.

        Args:
            old_activity (str): the activity to remove.

        Raises:
            TypeError: if old_activity is not a str.

        Returns:
            Project: the class instance itself.
        """
        if not isinstance(old_activity, str):
            raise TypeError("'old_activity' expect a str.")

        self.activities.remove(old_activity)
        return self

    def reorder_activity(self, order: list) -> "Project":
        """Reorder the activites attribute.

        Args:
            order (list): the new order of the activities attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Project: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.activities = [self.activities[i] for i in order]
        return self
