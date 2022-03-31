# -*- coding: utf-8 -*-
"""
work_experience.py
Author: Gilson, K.
"""

from typing import Any, List, Optional

from .mixin import JSONableMixin
from .project import Project


class WorkExperience(JSONableMixin):
    """WorkExperience: inherit from 'JSONableMixin'.

    Attributes:
        employer (str): name of the employer.
        start (int): start date of the experience under YYYYMM format.
        end (int, optional): end date of the experience under YYYYMM format. Defaults to None.
        position (str, optional): title of the position within the experience. Defaults to None.
        description (List[str], optional): list of paragraphs of the description. Defaults to None.
        projects (List[Project], optional): list of Project objects. Defaults to None.
    """

    def __init__(
        self,
        employer: str,
        start: int,
        end: Optional[int] = None,
        position: Optional[str] = None,
        description: Optional[List[str]] = None,
        projects: Optional[List[Project]] = None,
    ) -> None:
        """Initialize the WorkExperience class instance.

        Args:
            employer (str): name of the employer.
            start (int): start date of the experience under YYYYMM format.
            end (int, optional): end date of the experience under YYYYMM format. Defaults to None.
            position (str, optional): title of the position within the experience. Defaults to None.
            description (List[str], optional): list of paragraphs of the description. Defaults to None.
            projects (List[Project], optional): list of Project objects. Defaults to None.
        """
        self.employer = employer
        self.start = start
        self.end = end
        self.position = position
        self.description = description
        self.projects = projects

    def __setattr__(self, name: str, value: Any) -> None:
        """Validate the attributes of the WorkExperience class.

        Args:
            name (str): the name of the attribute.
            value (Any): the value of the attribute.

        Raises:
            TypeError: if 'employer' or 'position' are not a str.
            TypeError: if 'start' or 'end' are not an int.
            AttributeError: if 'start' or 'end' have and incorrect length.
            TypeError: if 'description' or 'projects' are not a list.
        """
        if value is not None:
            if name in ["employer", "position"] and not isinstance(value, str):
                raise TypeError(f"'{name}' expect a str.")
            elif name in ["start", "end"]:
                if not isinstance(value, int):
                    raise TypeError(f"'{name}' expect an int.")
                elif len(str(value)) != 6:
                    raise AttributeError(
                        f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format."
                    )
            elif name in ["description", "projects"] and not isinstance(value, list):
                raise TypeError(f"'{name}' expect a list.")

        self.__dict__[name] = value

    # Description
    def add_description(self, new_description: str) -> "WorkExperience":
        """Add a paragraph to the description attribute.

        Args:
            new_description (str): the paragraph to add.

        Raises:
            TypeError: if new_description is not a str.

        Returns:
            WorkExperience: the class instance itself.
        """
        if not isinstance(new_description, str):
            raise TypeError("'new_description' expect a str.")

        if self.description is None:
            self.description = []
        self.description.append(new_description)
        return self

    def remove_description(self, old_description: str) -> "WorkExperience":
        """Remove a paragraph from the description attribute.

        Args:
            old_description (str): the paragraph to remove.

        Raises:
            TypeError: if old_description is not a str.

        Returns:
            WorkExperience: the class instance itself.
        """
        if not isinstance(old_description, str):
            raise TypeError("'old_description' expect a str.")

        self.description.remove(old_description)
        return self

    def reorder_description(self, order: list) -> "WorkExperience":
        """Reorder the description attribute.

        Args:
            order (list): the new order of the description attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            WorkExperience: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.description = [self.description[i] for i in order]
        return self

    # Projects
    def add_project(self, new_project: Project) -> "WorkExperience":
        """Add a Project object to the projects attribute.

        Args:
            new_project (Project): the Project object to add.

        Raises:
            TypeError: if new_project is not a Project object.

        Returns:
            WorkExperience: the class instance itself.
        """
        if not isinstance(new_project, Project):
            raise TypeError("'new_project' expect a Project object.")

        if self.projects is None:
            self.projects = []
        self.projects.append(new_project)
        return self

    def remove_project(self, old_project: Project) -> "WorkExperience":
        """Remove a Project object from the projects attribute.

        Args:
            old_project (Project): the Project object to remove.

        Raises:
            TypeError: if old_project is not a Project object.

        Returns:
            WorkExperience: the class instance itself.
        """
        if not isinstance(old_project, Project):
            raise TypeError("'old_project' expect a Project object.")

        self.projects.remove(old_project)
        return self

    def reorder_project(self, order: list) -> "WorkExperience":
        """Reorder the projects attribute.

        Args:
            order (list): the new order of the projects attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            WorkExperience: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.projects = [self.projects[i] for i in order]
        return self

    # Sort
    def sort_projects(self, sort_type: Optional[str] = "asc") -> "WorkExperience":
        """Sort the projects attribute by their start and end dates.

        Args:
            sort_type (str, optional): the order of sorting. Defaults to "asc".

        Raises:
            TypeError: if sort_type is not a str.

        Returns:
            WorkExperience: the class instance itself.
        """
        if not isinstance(sort_type, str):
            raise TypeError("'sort_type' expect a str.")

        if sort_type == "desc":
            self.projects = sorted(
                self.projects, key=lambda x: (x.start, x.end), reverse=True
            )
        else:
            self.projects = sorted(
                self.projects, key=lambda x: (x.start, x.end), reverse=False
            )
        return self
