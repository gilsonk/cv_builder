# -*- coding: utf-8 -*-
"""
classes.py contains all the classes related to the cv_builder project.
"""
import json
from typing import List

class JSONableMixin(object):
    def to_dict(self, keep_none=True):
        dic = {}
        for key, value in self.__dict__.items():
            if isinstance(value, JSONableMixin):
                dic[key] = value.to_dict(keep_none)
            elif isinstance(value, list):
                lst = []
                for item in value:
                    if isinstance(item, JSONableMixin):
                        lst.append(item.to_dict(keep_none))
                    else:
                        if item is not None or keep_none == True:
                            lst.append(item)

                if lst or keep_none == True:
                    dic[key] = lst
            else:
                if value is not None or keep_none == True:
                    dic[key] = value

        return dic

class Language(JSONableMixin):
    """Language
    """
    def __init__(self,
                 name: str,
                 irl_scale: str=None,
                 cefr_level: str=None):
        self.name = name
        self.irl_scale = irl_scale
        self.cefr_level = cefr_level

    def __setattr__(self, name, value):
        # Validation
        if name == 'irl_scale' and value is not None:
            irl_list = [
                'No Proficiency',
                'Elementary Proficiency',
                'Limited Working Proficiency',
                'Professional Working Proficiency',
                'Full Professional Proficiency',
                'Bilingual',
                'Native'
            ]
            if value.title() not in irl_list:
                raise AttributeError(f"IRL Scale '{value}' unknown.\nShould be part of list:\n{irl_list}")
        elif name == 'cefr_level' and value is not None:
            cefr_list = [
                'A1',
                'A2',
                'B1',
                'B2',
                'C1',
                'C2'
            ]
            if value.upper() not in cefr_list:
                raise AttributeError(f"CEFR Level '{value}' unknown.\nShould be part of list:\n{cefr_list}")

        # Set
        if value is None:
            self.__dict__[name] = value
        else:
            if name == 'irl_scale':
                self.__dict__[name] = value.title()
            elif name == 'cefr_level':
                self.__dict__[name] = value.upper()
            else:
                self.__dict__[name] = value

class Education(JSONableMixin):
    """Education
    """
    def __init__(self,
                 school: str,
                 degree: str,
                 start: int,
                 end: int=None):
        self.school = school
        self.degree = degree
        self.start = start
        self.end = end

    def __setattr__(self, name, value):
        if name in ['start','end'] and value is not None:
            if len(str(value)) != 4:
                raise AttributeError(f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format.")

        self.__dict__[name] = value

class Project(JSONableMixin):
    """Projects
    """
    def __init__(self,
                 name: str=None,
                 redacted: str=None,
                 position: str=None,
                 start: int=None,
                 end: int=None,
                 description: List[str]=None,
                 activities: List[str]=None,
                 confidential: bool=True):
        self.name = name
        self.redacted = redacted
        self.position = position
        self.start = start
        self.end = end
        self.description = description
        self.activities = activities
        self.confidential = confidential

    def __setattr__(self, name, value):
        if name in ['start','end'] and value is not None:
            if len(str(value)) != 6:
                raise AttributeError(f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format.")

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

    # Activities
    def add_activity(self, new_activity):
        if self.activities is None:
            self.activities = []
        self.activities.append(new_activity)

    def remove_activity(self, old_activity):
        self.activities.remove(old_activity)

    def reorder_activity(self, order):
        self.activities = [self.activities[i] for i in order]

class WorkExperience(JSONableMixin):
    """Work Experience
    """
    def __init__(self,
                 employer: str,
                 start: int,
                 end: int=None,
                 position: str=None,
                 description: List[str]=None,
                 projects: List[Project]=None):
        self.employer = employer
        self.start = start
        self.end = end
        self.position = position
        self.description = description
        self.projects = projects

    def __setattr__(self, name, value):
        if name in ['start','end'] and value is not None:
            if len(str(value)) != 6:
                raise AttributeError(f"{name} '{value}' has an incorrect lenght.\nShould be 6 characters in the YYYYMM format.")

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
            self.projects = sorted(self.projects, key = lambda x: (x.start, x.end), reverse=False)
        elif sort_type == "desc":
            self.projects = sorted(self.projects, key = lambda x: (x.start, x.end), reverse=True)
        else:
            raise ValueError(f"Unknown sorting: {sort_type}.")

class Employee(JSONableMixin):
    """Employee
    """
    def __init__(self,
                 lastname: str,
                 firstname: str,
                 position: str,
                 languages: List[Language]=None,
                 summary: List[str]=None,
                 works: List[WorkExperience]=None,
                 trainings: List[str]=None,
                 itskills: List[str]=None,
                 educations: List[Education]=None):
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
            self.works = sorted(self.works, key = lambda x: (x.start, x.end), reverse=False)
        elif sort_type == "desc":
            self.works = sorted(self.works, key = lambda x: (x.start, x.end), reverse=True)
        else:
            raise ValueError(f"Unknown sorting: {sort_type}.")

    def sort_projects(self, sort_type):
        for work in self.works:
            if sort_type == "asc":
                work.projects = sorted(work.projects, key = lambda x: (x.start, x.end), reverse=False)
            elif sort_type == "desc":
                work.projects = sorted(work.projects, key = lambda x: (x.start, x.end), reverse=True)
            else:
                raise ValueError(f"Unknown sorting: {sort_type}.")

    def sort_educations(self, sort_type):
        if sort_type == "asc":
            self.educations = sorted(self.educations, key = lambda x: (x.start, x.end), reverse=False)
        elif sort_type == "desc":
            self.educations = sorted(self.educations, key = lambda x: (x.start, x.end), reverse=True)
        else:
            raise ValueError(f"Unknown sorting: {sort_type}.")

def remove_nulls(obj):
    if isinstance(obj, dict):
        return {key: value for key, value in obj.items() if value is not None}
    elif isinstance(obj, list):
        return [i for i in obj if obj[i] is not None ]

def load_employee(json_obj):
    # Create Employee
    new_employee = Employee(lastname=json_obj['lastname'],
                            firstname=json_obj['firstname'],
                            position=json_obj['position'])

    # Languages
    for language in json_obj['languages']:
        new_language = Language(**language)
        new_employee.add_language(new_language)

    # Summary
    if 'summary' in json_obj:
        for summary in json_obj['summary']:
            new_employee.add_summary(summary)

    # Works
    for work in json_obj['works']:
        new_work = WorkExperience(employer=work['employer'],
                                  start=work['start'])

        # End
        if 'end' in work:
            new_work.end = work['end']

        # Position
        if 'position' in work:
            new_work.position = work['position']

        # Description
        if 'description' in work:
            for description in work['description']:
                new_work.add_description(description)

        # Project
        if 'projects' in work:
            for project in work['projects']:
                new_project = Project(**project)
                new_work.add_project(new_project)

        new_employee.add_work(new_work)

    # Trainings
    if 'trainings' in json_obj:
        for training in json_obj['trainings']:
            new_employee.add_training(training)

    # IT Skills
    if 'itskills' in json_obj:
        for itskill in json_obj['itskills']:
            new_employee.add_itskill(itskill)

    # Education
    for education in json_obj['educations']:
        new_education = Education(**education)
        new_employee.add_education(new_education)

    return new_employee

def load_employee_json(json_path, json_encoding):
    # Load JSON
    with open(json_path, encoding=json_encoding) as json_file:
        json_obj = json.load(json_file, object_hook=remove_nulls)

    new_employee = load_employee(json_obj)

    return new_employee

if __name__ == "__main__":
    pass
