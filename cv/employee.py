# -*- coding: utf-8 -*-
"""
employee.py
Author: Gilson, K.
"""

import json
from typing import List

from .education import Education
from .language import Language
from .mixin import JSONableMixin
from .project import Project
from .work_experience import WorkExperience


class Employee(JSONableMixin):
    """Employee"""

    def __init__(
        self,
        lastname: str = None,
        firstname: str = None,
        position: str = None,
        languages: List[Language] = None,
        summary: List[str] = None,
        works: List[WorkExperience] = None,
        trainings: List[str] = None,
        itskills: List[str] = None,
        educations: List[Education] = None,
    ):
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
    def add_language(self, new_language):
        if self.languages is None:
            self.languages = []
        self.languages.append(new_language)

    def remove_language(self, old_language):
        self.languages.remove(old_language)

    def reorder_language(self, order):
        self.languages = [self.languages[i] for i in order]

    # Summary
    def add_summary(self, new_summary):
        if self.summary is None:
            self.summary = []
        self.summary.append(new_summary)

    def remove_summary(self, old_summary):
        self.summary.remove(old_summary)

    def reorder_summary(self, order):
        self.summary = [self.summary[i] for i in order]

    # Works
    def add_work(self, new_work):
        if self.works is None:
            self.works = []
        self.works.append(new_work)

    def remove_work(self, old_work):
        self.works.remove(old_work)

    def reorder_work(self, order):
        self.works = [self.works[i] for i in order]

    # Trainings
    def add_training(self, new_training):
        if self.trainings is None:
            self.trainings = []
        self.trainings.append(new_training)

    def remove_training(self, old_training):
        self.trainings.remove(old_training)

    def reorder_training(self, order):
        self.trainings = [self.trainings[i] for i in order]

    # IT Skills
    def add_itskill(self, new_itskill):
        if self.itskills is None:
            self.itskills = []
        self.itskills.append(new_itskill)

    def remove_itskill(self, old_itskill):
        self.itskills.remove(old_itskill)

    def reorder_itskills(self, order):
        self.itskills = [self.itskills[i] for i in order]

    # Education
    def add_education(self, new_education):
        if self.educations is None:
            self.educations = []
        self.educations.append(new_education)

    def remove_education(self, old_education):
        self.educations.remove(old_education)

    def reorder_education(self, order):
        self.educations = [self.educations[i] for i in order]

    # Sort
    def sort_works(self, sort_type):
        if sort_type == "asc":
            self.works = sorted(
                self.works, key=lambda x: (x.start, x.end), reverse=False
            )
        elif sort_type == "desc":
            self.works = sorted(
                self.works, key=lambda x: (x.start, x.end), reverse=True
            )
        else:
            raise ValueError(f"Unknown sorting: {sort_type}.")

    def sort_projects(self, sort_type):
        for work in self.works:
            if sort_type == "asc":
                work.projects = sorted(
                    work.projects, key=lambda x: (x.start, x.end), reverse=False
                )
            elif sort_type == "desc":
                work.projects = sorted(
                    work.projects, key=lambda x: (x.start, x.end), reverse=True
                )
            else:
                raise ValueError(f"Unknown sorting: {sort_type}.")

    def sort_educations(self, sort_type):
        if sort_type == "asc":
            self.educations = sorted(
                self.educations, key=lambda x: (x.start, x.end), reverse=False
            )
        elif sort_type == "desc":
            self.educations = sorted(
                self.educations, key=lambda x: (x.start, x.end), reverse=True
            )
        else:
            raise ValueError(f"Unknown sorting: {sort_type}.")

    @staticmethod
    def __remove_nulls(obj):
        if isinstance(obj, dict):
            return {key: value for key, value in obj.items() if value is not None}
        elif isinstance(obj, list):
            return [i for i in obj if obj[i] is not None]

    def load_from_json(self, json_path, json_encoding):
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
