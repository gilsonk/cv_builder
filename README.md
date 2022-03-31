[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# CV Builder

## Introduction
This project is written in Python and aim to automatically fill-in a CV template, based on a given JSON file.

## Dependencies
+ [Python-DOCX-Template](https://github.com/elapouya/python-docx-template)
+ [Jinja2](https://pypi.org/project/Jinja2/)
+ [Tkinter](https://docs.python.org/fr/3/library/tkinter.html)

## Usage
### With the compiled executable file (Windows only)
Within the **realeases**, download the latest executable file.

### Cloning it localy
Within a terminal, clone this repository and access it:

    git clone https://github.com/gilsonk/cv_builder.git
    cd cv_builder/

(Optional) Create a virtual environment:

    python -m venv PATH_TO_YOUR_ENV
    PATH_TO_YOUR_ENV/activate

Install dependencies:

    python -m pip install -r requirements.txt

Then run **cv_builder.py**:

    python cv_builder.py

### (Optional) Compiling it yourself
From within the cv_builder folder, run:

    pyinstaller --onefile --windowed cv_builder.py

## Data Model
In order to store CVs, the project define several custome classes, stored under a JSON format:
+ Employee class
  + Last Name (str)
  + First Name (str)
  + Position title (str)
  + Languages (list of Language objects)
    + Name (str)
    + IRL Scale (str)
    + CEFR Level (str)
  + Summaries (list of str)
  + Work Experiences (list of WorkExperience objects)
    + Employer (str)
    + Start date (int)
    + End date (int)
    + Position title (str)
    + Description (list of str)
    + Projects (list of Project objects)
      + Name (str)
      + Redacted name (str)
      + Position title (str)
      + Start date (int)
      + End date (int)
      + Description (list of str)
      + Activities (list of str)
      + Confidential (bool)
  + Trainings (list of str)
  + IT Skills (list of str)
  + Educations (list of Education objects)
    + School (str)
    + Degree (str)
    + Start year (int)
    + End year (int)

### Author
Gilson, Kevin
