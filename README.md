# TODO:
+ Create a front-end

# Introduction
This project is written in Python and aim to automatically fill-in a CV template, based on a given JSON file.

# Classes
The project define different custome classes:

### JSONableMixin
The JSONableMixin serve as a mixin for the next classes, and define a function
to recursively convert them to dictionaries.

### Language
The Language class define a language based on:
+ It's name;
+ The IRL Scale;
+ The CEFR Level.

### Education
The Education class define a degree based on:
+ The school;
+ The degree;
+ The degree start year;
+ The degree end year.

### Project
The Project class define a project based on:
+ It's name;
+ It's confidential name;
+ The job position;
+ The project start;
+ The project end;
+ A list of descriptions;
+ A list of activities;
+ Whether the project should be treated as confidential or not.

### WorkExperience
The WorkExperience class define a work experience based on:
+ The employer;
+ The employment start date;
+ The employment end date;
+ The position;
+ A list of descriptions;
+ A list of Projects.

### Employee
The Employee class define and employee based on:
+ It's last name;
+ It's first name;
+ It's position;
+ A list of Language;
+ A list of summaries;
+ A list of WorkExperience;
+ A list of trainings;
+ A list of IT Skills;
+ A list of Education.

# Dependencies
+ [Python-DOCX-Template](https://github.com/elapouya/python-docx-template)
+ [Jinja2](https://pypi.org/project/Jinja2/)

## Author
Gilson, Kevin
