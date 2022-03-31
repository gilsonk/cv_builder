# -*- coding: utf-8 -*-
"""
employee.py
Author: Gilson, K.
"""

import json
from typing import List, Optional, Union

from .education import Education
from .language import Language
from .mixin import JSONableMixin
from .project import Project
from .work_experience import WorkExperience


class Employee(JSONableMixin):
    """Employee: inherit from 'JSONableMixin'.

    Attributes:
        lastname (str, optional): last name of the employee.
        firstname (str, optional): first name of the employee.
        position (str, optional): title of the position of the employee.
        languages (List[Language], optional): list of Language objects. Defaults to None.
        summary (List[str], optional): list of paragraphs of the summary. Defaults to None.
        works (List[WorkExperience], optional): list of WorkExperience objects. Defaults to None.
        trainings (List[str], optional): list of trainings. Defaults to None.
        itskills (List[str], optional): list of IT Skills. Defaults to None.
        educations (List[Education], optional): list of Education objects. Defaults to None.
    """

    def __init__(
        self,
        lastname: Optional[str] = None,
        firstname: Optional[str] = None,
        position: Optional[str] = None,
        languages: Optional[List[Language]] = None,
        summary: Optional[List[str]] = None,
        works: Optional[List[WorkExperience]] = None,
        trainings: Optional[List[str]] = None,
        itskills: Optional[List[str]] = None,
        educations: Optional[List[Education]] = None,
    ) -> None:
        """Initialize the Employee class instance.

        Args:
            lastname (str, optional): last name of the employee.
            firstname (str, optional): first name of the employee.
            position (str, optional): title of the position of the employee.
            languages (List[Language], optional): list of Language objects. Defaults to None.
            summary (List[str], optional): list of paragraphs of the summary. Defaults to None.
            works (List[WorkExperience], optional): list of WorkExperience objects. Defaults to None.
            trainings (List[str], optional): list of trainings. Defaults to None.
            itskills (List[str], optional): list of IT Skills. Defaults to None.
            educations (List[Education], optional): list of Education objects. Defaults to None.
        """
        self.lastname = lastname
        self.firstname = firstname
        self.position = position
        self.languages = languages
        self.summary = summary
        self.works = works
        self.trainings = trainings
        self.itskills = itskills
        self.educations = educations

    # Languages
    def add_language(self, new_language: Language) -> "Employee":
        """Add a Language object to the languages attribue.

        Args:
            new_language (Language): the Language object to add.

        Raises:
            TypeError: if new_language is not a Language object.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(new_language, Language):
            raise TypeError("'new_language' expect a Language object.")

        if self.languages is None:
            self.languages = []
        self.languages.append(new_language)
        return self

    def remove_language(self, old_language: Language) -> "Employee":
        """Remove a Language object from the languages attribute.

        Args:
            old_language (Language): the Language object to remove.

        Raises:
            TypeError: if old_language is not a Language object.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(old_language, Language):
            raise TypeError("'old_language' expect a Language object.")

        self.languages.remove(old_language)
        return self

    def reorder_languages(self, order: list) -> "Employee":
        """Reorder the languages attribute.

        Args:
            order (list): the new order of the languages attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.languages = [self.languages[i] for i in order]
        return self

    # Summary
    def add_summary(self, new_summary: str) -> "Employee":
        """Add a paragraph string to the summary attribute.

        Args:
            new_summary (str): the paragraph to add.

        Raises:
            TypeError: if new_summary is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(new_summary, str):
            raise TypeError("'new_summary' expect a str.")

        if self.summary is None:
            self.summary = []
        self.summary.append(new_summary)
        return self

    def remove_summary(self, old_summary: str) -> "Employee":
        """Remove a paragraph string from the summary attribute.

        Args:
            old_summary (str): the paragraph to remove.

        Raises:
            TypeError: if old_summary is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(old_summary, str):
            raise TypeError("'old_summary' expect a str.")

        self.summary.remove(old_summary)
        return self

    def reorder_summary(self, order: list) -> "Employee":
        """Reorder the summary attribute.

        Args:
            order (list): the new order of the summary attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.summary = [self.summary[i] for i in order]
        return self

    # Works
    def add_work(self, new_work: WorkExperience) -> "Employee":
        """Add a WorkExperience object to the works attribute.

        Args:
            new_work (WorkExperience): the WorkExperience object to add.

        Raises:
            TypeError: if new_work is not a WorkExperience object.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(new_work, WorkExperience):
            raise TypeError("'new_work' expect a WorkExperience object")

        if self.works is None:
            self.works = []
        self.works.append(new_work)
        return self

    def remove_work(self, old_work: WorkExperience) -> "Employee":
        """Remove a WorkExperience object from the works attribute.

        Args:
            old_work (WorkExperience): the WorkExperience object to remove.

        Raises:
            TypeError: if old_work is not a WorkExperience object.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(old_work, WorkExperience):
            raise TypeError("'old_work' expect a WorkExperience object.")

        self.works.remove(old_work)
        return self

    def reorder_works(self, order: list) -> "Employee":
        """Reorder the works attribute.

        Args:
            order (list): the new order of the works attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.works = [self.works[i] for i in order]
        return self

    # Trainings
    def add_training(self, new_training: str) -> "Employee":
        """Add a training paragraph to the trainings attribute.

        Args:
            new_training (str): the paragraph to add.

        Raises:
            TypeError: if new_training is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(new_training, str):
            raise TypeError("'new_training' expect a str.")

        if self.trainings is None:
            self.trainings = []
        self.trainings.append(new_training)
        return self

    def remove_training(self, old_training: str) -> "Employee":
        """Remove a training paragraph from the trainings attribute.

        Args:
            old_training (str): the paragraph to remove.

        Raises:
            TypeError: if old_training is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(old_training, str):
            raise TypeError("'old_training' expect a str.")

        self.trainings.remove(old_training)
        return self

    def reorder_trainings(self, order: list) -> "Employee":
        """Reorder the trainings attribute.

        Args:
            order (list): the new order of the trainings attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.trainings = [self.trainings[i] for i in order]
        return self

    # IT Skills
    def add_itskill(self, new_itskill: str) -> "Employee":
        """Add an IT skill paragraph to the itskills attribute.

        Args:
            new_itskill (str): the paragraph to add.

        Raises:
            TypeError: if new_itskill is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(new_itskill, str):
            raise TypeError("'new_itskill' expect a str.")

        if self.itskills is None:
            self.itskills = []
        self.itskills.append(new_itskill)
        return self

    def remove_itskill(self, old_itskill: str) -> "Employee":
        """Remove an IT skill paragraph from the itskills attribute.

        Args:
            old_itskill (str): the paragraph to remove.

        Raises:
            TypeError: if old_itskill is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(old_itskill, str):
            raise TypeError("'old_itskill' expect a str.")

        self.itskills.remove(old_itskill)
        return self

    def reorder_itskills(self, order: list) -> "Employee":
        """Reorder the itskills attribute.

        Args:
            order (list): the new order of the itskills attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.itskills = [self.itskills[i] for i in order]
        return self

    # Education
    def add_education(self, new_education: Education) -> "Employee":
        """Add an Education object to the educations attribute.

        Args:
            new_education (Education): the Education object to add.

        Raises:
            TypeError: if new_education is not an Education object.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(new_education, Education):
            raise TypeError("'new_education' expect an Education object.")

        if self.educations is None:
            self.educations = []
        self.educations.append(new_education)
        return self

    def remove_education(self, old_education: Education) -> "Employee":
        """Remove an Education object from the educations attribute.

        Args:
            old_education (Education): the Education object to remove.

        Raises:
            TypeError: if old_education is not an Education object.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(old_education, Education):
            raise TypeError("'old_education' expect an Education object.")

        self.educations.remove(old_education)
        return self

    def reorder_educations(self, order: list) -> "Employee":
        """Reorder the educations attribute.

        Args:
            order (list): the new order of the educations attribute.

        Raises:
            TypeError: if order is not a list.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.educations = [self.educations[i] for i in order]
        return self

    # Sort
    def sort_works(self, sort_type: Optional[str] = "asc") -> "Employee":
        """Sort the works attribute by their start and end dates.

        Args:
            sort_type (str, optional): the order of sorting. Defaults to "asc".

        Raises:
            TypeError: if sort_type is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(sort_type, str):
            raise TypeError("'sort_type' expect a str.")

        if sort_type == "desc":
            self.works = sorted(
                self.works, key=lambda x: (x.start, x.end), reverse=True
            )
        else:
            self.works = sorted(
                self.works, key=lambda x: (x.start, x.end), reverse=False
            )
        return self

    def sort_projects(self, sort_type: Optional[str] = "asc") -> "Employee":
        """For each WorkExperience within the works attribute, sort their project by their start and end dates.

        Args:
            sort_type (str, optional): the order of sorting. Defaults to "asc".

        Raises:
            TypeError: if sort_type is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(sort_type, str):
            raise TypeError("'sort_type' expect a str.")

        for work in self.works:
            if sort_type == "desc":
                work.projects = sorted(
                    work.projects, key=lambda x: (x.start, x.end), reverse=True
                )
            else:
                work.projects = sorted(
                    work.projects, key=lambda x: (x.start, x.end), reverse=False
                )
            return self

    def sort_educations(self, sort_type: Optional[str] = "asc") -> "Employee":
        """Sort the educations attribute by their start and end dates.

        Args:
            sort_type (str, optional): the order of sorting. Defaults to "asc".

        Raises:
            TypeError: if sort_type is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(sort_type, str):
            raise TypeError("'sort_type' expect a str.")

        if sort_type == "desc":
            self.educations = sorted(
                self.educations, key=lambda x: (x.start, x.end), reverse=True
            )
        else:
            self.educations = sorted(
                self.educations, key=lambda x: (x.start, x.end), reverse=False
            )
        return self

    @staticmethod
    def __remove_nulls(obj: Union[dict, list]) -> Union[dict, list]:
        """Object hook function to remove None values from either a dict or a list.

        Args:
            obj (Union[dict, list]): the object to parse.

        Raises:
            TypeError: when the object passed as input is neither a dict, nor a list.

        Returns:
            Union[dict, list]: the input object purged from its None values.
        """
        if isinstance(obj, dict):
            return {key: value for key, value in obj.items() if value is not None}
        elif isinstance(obj, list):
            return [i for i in obj if obj[i] is not None]
        raise TypeError(f"'{obj}' expect a dict or a list'")

    def load_from_json(self, json_path: str, json_encoding: str) -> "Employee":
        """Populate the current instance from a JSON file.

        Args:
            json_path (str): the JSON file path.
            json_encoding (str): the encoding of the file.

        Raises:
            TypeError: if json_path is not a str.
            TypeError: if json_encoding is not a str.

        Returns:
            Employee: the class instance itself.
        """
        if not isinstance(json_path, str):
            raise TypeError("'json_path' expect a str.")
        elif not isinstance(json_encoding, str):
            raise TypeError("'json_encoding' expect a str.")

        # Open JSON file
        with open(json_path, encoding=json_encoding) as json_file:
            json_obj = json.load(json_file, object_hook=self.__remove_nulls)

        self.lastname = json_obj["lastname"]
        self.firstname = json_obj["firstname"]
        self.position = json_obj["position"]

        # Languages
        for language in json_obj["languages"]:
            new_language = Language(**language)
            self.add_language(new_language)

        # Summary
        if "summary" in json_obj:
            for summary in json_obj["summary"]:
                self.add_summary(summary)

        # Works
        for work in json_obj["works"]:
            new_work = WorkExperience(employer=work["employer"], start=work["start"])

            # End
            if "end" in work:
                new_work.end = work["end"]

            # Position
            if "position" in work:
                new_work.position = work["position"]

            # Description
            if "description" in work:
                for description in work["description"]:
                    new_work.add_description(description)

            # Project
            if "projects" in work:
                for project in work["projects"]:
                    new_project = Project(**project)
                    new_work.add_project(new_project)

            self.add_work(new_work)

        # Trainings
        if "trainings" in json_obj:
            for training in json_obj["trainings"]:
                self.add_training(training)

        # IT Skills
        if "itskills" in json_obj:
            for itskill in json_obj["itskills"]:
                self.add_itskill(itskill)

        # Education
        for education in json_obj["educations"]:
            new_education = Education(**education)
            self.add_education(new_education)

        return self
