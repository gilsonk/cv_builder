# -*- coding: utf-8 -*-
"""
work_experience.py
Author: Gilson, K.
"""

from typing import List

from .mixin import JSONableMixin
from .project import Project


class WorkExperience(JSONableMixin):
    """Work Experience"""

    def __init__(
        self,
        employer: str,
        start: int,
        end: int = None,
        position: str = None,
        description: List[str] = None,
        projects: List[Project] = None,
    ):
        self.employer = employer
        self.start = start
        self.end = end
        self.position = position
        self.description = description
        self.projects = projects

    def __setattr__(self, name, value):
        if name in ["start", "end"] and value is not None:
            if len(str(value)) != 6:
                raise AttributeError(
                    f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format."
                )

        self.__dict__[name] = value

    # Description
    def add_description(self, new_description):
        if self.description is None:
            self.description = []
        self.description.append(new_description)

    def remove_description(self, old_description):
        self.description.remove(old_description)

    def reorder_description(self, order):
        self.description = [self.description[i] for i in order]

    # Projects
    def add_project(self, new_project):
        if self.projects is None:
            self.projects = []
        self.projects.append(new_project)

    def remove_project(self, old_project):
        self.projects.remove(old_project)

    def reorder_project(self, order):
        self.projects = [self.projects[i] for i in order]

    # Sort
    def sort_projects(self, sort_type):
        if sort_type == "asc":
            self.projects = sorted(
                self.projects, key=lambda x: (x.start, x.end), reverse=False
            )
        elif sort_type == "desc":
            self.projects = sorted(
                self.projects, key=lambda x: (x.start, x.end), reverse=True
            )
        else:
            raise ValueError(f"Unknown sorting: {sort_type}.")
