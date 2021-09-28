# -*- coding: utf-8 -*-
"""
main.py contains the mail back-end flow of the cv_builder project.
"""
import classes as cl
import os

from docxtpl import DocxTemplate
import jinja2

def open_subfiles(file_path):
    script_file = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_file)
    abs_file_path = os.path.join(script_dir, file_path)
    return abs_file_path

def format_date(date_int):
    months_dic = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    if date_int is None:
        return "Ongoing"
    else:
        date_str = str(date_int)
        year = date_str[0:4]
        month = months_dic[date_str[-2:]]
        return f"{month} {year}"

def main():
    # Load employee
    new_employee = cl.load_employee_json(open_subfiles("cvs/example.json"), 'utf-8')

    # Sort by descending
    new_employee.sort_works("desc")
    new_employee.sort_projects("desc")
    new_employee.sort_educations("desc")

    # Load template
    doc = DocxTemplate(open_subfiles("templates/example.docx"))

    # Load Jinja env
    jinja_env = jinja2.Environment()
    jinja_env.filters['format_date'] = format_date

    # Set context
    context = new_employee.to_dict(keep_none=False)

    # Export
    doc.render(context, jinja_env=jinja_env, autoescape=True)
    doc.save("generated_doc.docx")
    print("Done.")

if __name__ == "__main__":
    main()
