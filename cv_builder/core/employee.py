# -*- coding: utf-8 -*-
"""The 'employee' module of the 'core' package contains classes related to the Employee layer of the data model."""

import json
from typing import List, Optional, Union

from cv_builder.core.education import Education
from cv_builder.core.language import Language
from cv_builder.core.mixin import JSONableMixin
from cv_builder.core.project import Project
from cv_builder.core.work_experience import WorkExperience


class Employee(JSONableMixin):
    """Representation of an Employee characteristics.

    Parameters
    ----------
    lastname : str, optional
        Last name of the employee, by default None.
    firstname : str, optional
        First name of the employee, by default None.
    position : str, optional
        Title of the position of the employee, by default None.
    languages : List[Language], optional
        List of Language objects, by default None.
    summary : List[str], optional
        List of paragraphs of the summary, by default None.
    works : List[WorkExperience], optional
        List of WorkExperience objects, by default None.
    trainings : List[str], optional
        List of trainings, by default None.
    itskills : List[str], optional
        List of IT Skills, by default None.
    educations : List[Education], optional
        List of Education objects, by default None.
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
        """Initialize the Employee class instance."""
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
        """Add a Language object to the languages attribute.

        Parameters
        ----------
        new_language : Language
            The Language object to add.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        TypeError
            If new_language is not a Language object.
        """
        if not isinstance(new_language, Language):
            raise TypeError("'new_language' expect a Language object.")

        if self.languages is None:
            self.languages = []
        self.languages.append(new_language)
        return self

    def remove_language(self, old_language: Language) -> "Employee":
        """Remove a Language object from the languages attribute.

        Parameters
        ----------
        old_language : Language
            The Language object to remove.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If languages are empty.
        TypeError
            If old_language is not a Language object.
        """
        if self.languages is None:
            raise ValueError("'languages' is empty.")
        if not isinstance(old_language, Language):
            raise TypeError("'old_language' expect a Language object.")

        self.languages.remove(old_language)
        return self

    def reorder_languages(self, order: List[int]) -> "Employee":
        """Reorder the languages attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the languages attribute.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If languages are empty.
        TypeError
            If order is not a list.
        """
        if self.languages is None:
            raise ValueError("'languages' is empty.")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.languages = [self.languages[i] for i in order]
        return self

    # Summary
    def add_summary(self, new_summary: str) -> "Employee":
        """Add a paragraph string to the summary attribute.

        Parameters
        ----------
        new_summary : str
            The paragraph to add.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        TypeError
            If new_summary is not a str.
        """
        if not isinstance(new_summary, str):
            raise TypeError("'new_summary' expect a str.")

        if self.summary is None:
            self.summary = []
        self.summary.append(new_summary)
        return self

    def remove_summary(self, old_summary: str) -> "Employee":
        """Remove a paragraph string from the summary attribute.

        Parameters
        ----------
        old_summary : str
            The paragraph to remove.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If summary is empty.
        TypeError
            If old_summary is not a str.
        """
        if self.summary is None:
            raise ValueError("'summary' is empty.")
        if not isinstance(old_summary, str):
            raise TypeError("'old_summary' expect a str.")

        self.summary.remove(old_summary)
        return self

    def reorder_summary(self, order: List[int]) -> "Employee":
        """Reorder the summary attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the summary attribute.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If summary is empty.
        TypeError
            If order is not a list.
        """
        if self.summary is None:
            raise ValueError("'summary' is empty.")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.summary = [self.summary[i] for i in order]
        return self

    # Works
    def add_work(self, new_work: WorkExperience) -> "Employee":
        """Add a WorkExperience object to the works attribute.

        Parameters
        ----------
        new_work : WorkExperience
            The WorkExperience object to add.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        TypeError
            If new_work is not a WorkExperience object.
        """
        if not isinstance(new_work, WorkExperience):
            raise TypeError("'new_work' expect a WorkExperience object")

        if self.works is None:
            self.works = []
        self.works.append(new_work)
        return self

    def remove_work(self, old_work: WorkExperience) -> "Employee":
        """Remove a WorkExperience object from the works attribute.

        Parameters
        ----------
        old_work : WorkExperience
            The WorkExperience object to remove.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If works are empty.
        TypeError
            If old_work is not a WorkExperience object.
        """
        if self.works is None:
            raise ValueError("'works' is empty.")
        if not isinstance(old_work, WorkExperience):
            raise TypeError("'old_work' expect a WorkExperience object.")

        self.works.remove(old_work)
        return self

    def reorder_works(self, order: List[int]) -> "Employee":
        """Reorder the works attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the works attribute.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If works are empty.
        TypeError
            If order is not a list.
        """
        if self.works is None:
            raise ValueError("'works' is empty.")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.works = [self.works[i] for i in order]
        return self

    # Trainings
    def add_training(self, new_training: str) -> "Employee":
        """Add a training paragraph to the trainings attribute.

        Parameters
        ----------
        new_training : str
            The paragraph to add.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        TypeError
            If new_training is not a str.
        """
        if not isinstance(new_training, str):
            raise TypeError("'new_training' expect a str.")

        if self.trainings is None:
            self.trainings = []
        self.trainings.append(new_training)
        return self

    def remove_training(self, old_training: str) -> "Employee":
        """Remove a training paragraph from the trainings attribute.

        Parameters
        ----------
        old_training : str
            The paragraph to remove.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If trainings are empty.
        TypeError
            If old_training is not a str.
        """
        if self.trainings is None:
            raise ValueError("'trainings' is empty.")
        if not isinstance(old_training, str):
            raise TypeError("'old_training' expect a str.")

        self.trainings.remove(old_training)
        return self

    def reorder_trainings(self, order: List[int]) -> "Employee":
        """Reorder the trainings attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the trainings attribute.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If trainings are empty.
        TypeError
            If order is not a list.
        """
        if self.trainings is None:
            raise ValueError("'trainings' is empty.")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.trainings = [self.trainings[i] for i in order]
        return self

    # IT Skills
    def add_itskill(self, new_itskill: str) -> "Employee":
        """Add an IT skill paragraph to the itskills attribute.

        Parameters
        ----------
        new_itskill : str
            The paragraph to add.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        TypeError
            If new_itskill is not a str.
        """
        if not isinstance(new_itskill, str):
            raise TypeError("'new_itskill' expect a str.")

        if self.itskills is None:
            self.itskills = []
        self.itskills.append(new_itskill)
        return self

    def remove_itskill(self, old_itskill: str) -> "Employee":
        """Remove an IT skill paragraph from the itskills attribute.

        Parameters
        ----------
        old_itskill : str
            The paragraph to remove.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If itskills are empty.
        TypeError
            If old_itskill is not a str.
        """
        if self.itskills is None:
            raise ValueError("'itskills' are empty.")
        if not isinstance(old_itskill, str):
            raise TypeError("'old_itskill' expect a str.")

        self.itskills.remove(old_itskill)
        return self

    def reorder_itskills(self, order: List[int]) -> "Employee":
        """Reorder the itskills attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the itskills attribute.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If itskills are empty.
        TypeError
            If order is not a list.
        """
        if self.itskills is None:
            raise ValueError("'itskills' are empty.")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.itskills = [self.itskills[i] for i in order]
        return self

    # Education
    def add_education(self, new_education: Education) -> "Employee":
        """Add an Education object to the educations attribute.

        Parameters
        ----------
        new_education : Education
            The Education object to add.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        TypeError
            If new_education is not an Education object.
        """
        if not isinstance(new_education, Education):
            raise TypeError("'new_education' expect an Education object.")

        if self.educations is None:
            self.educations = []
        self.educations.append(new_education)
        return self

    def remove_education(self, old_education: Education) -> "Employee":
        """Remove an Education object from the educations attribute.

        Parameters
        ----------
        old_education : Education
            The Education object to remove.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If educations are empty.
        TypeError
            If old_education is not an Education object.
        """
        if self.educations is None:
            raise ValueError("'educations' is empty.")
        if not isinstance(old_education, Education):
            raise TypeError("'old_education' expect an Education object.")

        self.educations.remove(old_education)
        return self

    def reorder_educations(self, order: List[int]) -> "Employee":
        """Reorder the educations attribute.

        Parameters
        ----------
        order : List[int]
            The new order of the educations attribute.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If educations are empty.
        TypeError
            If order is not a list.
        """
        if self.educations is None:
            raise ValueError("'educations' is empty.")
        if not isinstance(order, list):
            raise TypeError("'order' expect a list.")

        self.educations = [self.educations[i] for i in order]
        return self

    # Sort
    def sort_works(self, sort_type: Optional[str] = "asc") -> "Employee":
        """Sort the works attribute by their start and end dates.

        Parameters
        ----------
        sort_type : str, optional
            The order of sorting, by default "asc".

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If works are empty.
        TypeError
            If sort_type is not a str.
        """
        if self.works is None:
            raise ValueError("'works' is empty.")
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

        Parameters
        ----------
        sort_type : str, optional
            The order of sorting, by default "asc".

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If works are empty.
        TypeError
            If sort_type is not a str.
        ValueError
            If any work projects are empty.
        """
        if self.works is None:
            raise ValueError("'works' is empty.")
        if not isinstance(sort_type, str):
            raise TypeError("'sort_type' expect a str.")

        for work in self.works:
            if work.projects is None:
                raise ValueError("'projects' is empty.")
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

        Parameters
        ----------
        sort_type : str, optional
            The order of sorting, by default "asc".

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        ValueError
            If educations are empty.
        TypeError
            If sort_type is not a str.
        """
        if self.educations is None:
            raise ValueError("'educations' is empty.")
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

        Parameters
        ----------
        obj : Union[dict, list]
            The object to parse.

        Returns
        -------
        Union[dict, list]
            The input object purged from its None values.

        Raises
        ------
        TypeError
            When the object passed as input is neither a dict, nor a list.
        """
        if isinstance(obj, dict):
            return {key: value for key, value in obj.items() if value is not None}
        elif isinstance(obj, list):
            return [i for i in obj if obj[i] is not None]
        raise TypeError(f"'{obj}' expect a dict or a list'")

    def load_from_json(self, json_path: str, json_encoding: str) -> "Employee":
        """Populate the current instance from a JSON file.

        Parameters
        ----------
        json_path : str
            The JSON file path.
        json_encoding : str
            The encoding of the file.

        Returns
        -------
        Employee
            The class instance itself.

        Raises
        ------
        TypeError
            If json_path is not a str.
        TypeError
            If json_encoding is not a str.
        """
        if not isinstance(json_path, str):
            raise TypeError("'json_path' expect a str.")
        if not isinstance(json_encoding, str):
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
