# -*- coding: utf-8 -*-
"""The 'project' module of the 'core' package contains classes related to the Project layer of the data model."""

from typing import Any, List, Optional

from cv_builder.core.mixin import JSONableMixin


class Project(JSONableMixin):
    """Representation of a professional Project attributes.

    Parameters
    ----------
    name : str, optional
        Name of the project, by default None.
    redacted : str, optional
        Confidential proxy name of the project, by default None.
    position : str, optional
        Title of the position within the project, by default None.
    start : int, optional
        Start date of the project under YYYYMM format, by default None.
    end : int, optional
        End date of the project under YYYYMM format, by default None.
    description : List[str], optional
        List of paragraphs of the description, by default None.
    activities : List[str], optional
        List of the activities, by default None.
    confidential : bool, optional
        Whether to treat the project as confidential or not, by default None.
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
        """Initialize the Project class instance."""
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

        Parameters
        ----------
        name : str
            The name of the attribute.
        value : Any
            The value of the attribute.

        Raises
        ------
        TypeError
            If 'name', 'redacted', or 'position' are not str.
        TypeError
            If 'start' or 'end' are not an int.
        AttributeError
            If 'start' or 'end' have and incorrect length.
        TypeError
            If 'description' or 'activities' are not a list.
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

        Parameters
        ----------
        new_description : str
            The paragraph to add.

        Returns
        -------
        Project
            The class instance itself.

        Raises
        ------
        TypeError
            If new_description is not a str.
        """
        if not isinstance(new_description, str):
            raise TypeError("'new_description' expect a str.")

        if self.description is None:
            self.description = []
        self.description.append(new_description)
        return self

    def remove_description(self, old_description: str) -> "Project":
        """Remove a paragraph from the description attribute.

        Parameters
        ----------
        old_description : str
            The paragraph to remove.

        Returns
        -------
        Project
            The class instance itself.

        Raises
        ------
        TypeError
            If old_description is not a str.
        """
        if not isinstance(old_description, str):
            raise TypeError("'old_description' expect a str.")

        self.description.remove(old_description)
        return self

    def reorder_description(self, order: List[int]) -> "Project":
        """Reorder the description attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the description attribute.

        Returns
        -------
        Project
            The class instance itself.

        Raises
        ------
        TypeError
            If order is not a list.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.description = [self.description[i] for i in order]
        return self

    # Activities
    def add_activity(self, new_activity: str) -> "Project":
        """Add an activity to the activities attribute.

        Parameters
        ----------
        new_activity : str
            The activity to add.

        Returns
        -------
        Project
            The class instance itself.

        Raises
        ------
        TypeError
            If new_activity is not a str.
        """
        if not isinstance(new_activity, str):
            raise TypeError("'new_activity' expect a str.")

        if self.activities is None:
            self.activities = []
        self.activities.append(new_activity)
        return self

    def remove_activity(self, old_activity: str) -> "Project":
        """Remove an activity from the activities attribute.

        Parameters
        ----------
        old_activity : str
            The activity to remove.

        Returns
        -------
        Project
            The class instance itself.

        Raises
        ------
        TypeError
            If old_activity is not a str.
        """
        if not isinstance(old_activity, str):
            raise TypeError("'old_activity' expect a str.")

        self.activities.remove(old_activity)
        return self

    def reorder_activity(self, order: List[int]) -> "Project":
        """Reorder the activities attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the activities attribute.

        Returns
        -------
        Project
            The class instance itself.

        Raises
        ------
        TypeError
            If order is not a list.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.activities = [self.activities[i] for i in order]
        return self
