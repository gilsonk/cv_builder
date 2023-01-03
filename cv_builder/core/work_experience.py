# -*- coding: utf-8 -*-
"""The 'work_experience' module of the 'core' package contains classes related to the Work layer of the data model."""

from typing import Any, List, Optional

from cv_builder.core.mixin import JSONableMixin
from cv_builder.core.project import Project


class WorkExperience(JSONableMixin):
    """Representation of a Work Experience attributes.

    Parameters
    ----------
    employer : str
        Name of the employer.
    start : int
        Start date of the experience under YYYYMM format.
    end : int, optional
        End date of the experience under YYYYMM format, by default None.
    position : str, optional
        Title of the position within the experience, by default None.
    description : List[str], optional
        List of paragraphs of the description, by default None.
    projects : List[Project], optional
        List of Project objects, by default None.
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
        """Initialize the WorkExperience class instance."""
        self.employer = employer
        self.start = start
        self.end = end
        self.position = position
        self.description = description
        self.projects = projects

    def __setattr__(self, name: str, value: Any) -> None:
        """Validate the attributes of the WorkExperience class.

        Parameters
        ----------
        name : str
            The name of the attribute.
        value : Any
            The value of the attribute.

        Raises
        ------
        TypeError
            If 'employer' or 'position' are not a str.
        TypeError
            If 'start' or 'end' are not an int.
        AttributeError
            If 'start' or 'end' have and incorrect length.
        TypeError
            If 'description' or 'projects' are not a list.
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

        Parameters
        ----------
        new_description : str
            The paragraph to add.

        Returns
        -------
        WorkExperience
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

    def remove_description(self, old_description: str) -> "WorkExperience":
        """Remove a paragraph from the description attribute.

        Parameters
        ----------
        old_description : str
            The paragraph to remove.

        Returns
        -------
        WorkExperience
            The class instance itself.

        Raises
        ------
        ValueError
            If description is empty.
        TypeError
            If old_description is not a str.
        """
        if self.description is None:
            raise ValueError("'description' is empty.")
        if not isinstance(old_description, str):
            raise TypeError("'old_description' expect a str.")

        self.description.remove(old_description)
        return self

    def reorder_description(self, order: List[int]) -> "WorkExperience":
        """Reorder the description attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the description attribute.

        Returns
        -------
        WorkExperience
            The class instance itself.

        Raises
        ------
        ValueError
            If description is empty.
        TypeError
            If order is not a list.
        """
        if self.description is None:
            raise ValueError("'description' is empty.")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.description = [self.description[i] for i in order]
        return self

    # Projects
    def add_project(self, new_project: Project) -> "WorkExperience":
        """Add a Project object to the projects attribute.

        Parameters
        ----------
        new_project : Project
            The Project object to add.

        Returns
        -------
        WorkExperience
            The class instance itself.

        Raises
        ------
        TypeError
            If new_project is not a Project object.
        """
        if not isinstance(new_project, Project):
            raise TypeError("'new_project' expect a Project object.")

        if self.projects is None:
            self.projects = []
        self.projects.append(new_project)
        return self

    def remove_project(self, old_project: Project) -> "WorkExperience":
        """Remove a Project object from the projects attribute.

        Parameters
        ----------
        old_project : Project
            The Project object to remove.

        Returns
        -------
        WorkExperience
            The class instance itself.

        Raises
        ------
        ValueError
            If projects are empty.
        TypeError
            If old_project is not a Project object.
        """
        if self.projects is None:
            raise ValueError("'projects' is empty.'")
        if not isinstance(old_project, Project):
            raise TypeError("'old_project' expect a Project object.")

        self.projects.remove(old_project)
        return self

    def reorder_project(self, order: List[int]) -> "WorkExperience":
        """Reorder the projects attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the projects attribute.

        Returns
        -------
        WorkExperience
            The class instance itself.

        Raises
        ------
        ValueError
            If projects are empty.
        TypeError
            If order is not a list.
        """
        if self.projects is None:
            raise ValueError("'projects' is empty.'")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.projects = [self.projects[i] for i in order]
        return self

    # Sort
    def sort_projects(self, sort_type: Optional[str] = "asc") -> "WorkExperience":
        """Sort the projects attribute by their start and end dates.

        Parameters
        ----------
        sort_type : str, optional
            The order of sorting, by default None.

        Returns
        -------
        WorkExperience
            The class instance itself.

        Raises
        ------
        ValueError
            If projects are empty.
        TypeError
            If sort_type is not a str.
        """
        if self.projects is None:
            raise ValueError("'projects' is empty.'")
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
