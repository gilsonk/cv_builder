
# -*- coding: utf-8 -*-
"""
gui.py contains the GUI of the cv_builder project.
For CV Builder, should have:
1. Select between upload or create
   Combobox?
    1.a. If upload, load file
2. Notebook windows with different categories
    Possibilities to edit categories
    Spinbox for dates
    Scrolltext for edits
    Treeview with checkbox for selection
        Select / Deselect all
        Move up / down
        Redact all / Show all
    Button to run template that open a file dialog
        Two field, template path, saving path
    Button to export to
        Word
        Pdf
TODO:
* Link GUI with functions
* Work Experience layout
"""
import textwrap
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
import ttkwidgets

class CheckboxTreeviewFrame(ttk.LabelFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        padding = {
            'padx': 5,
            'pady': 5
        }

        # Tree
        columns= []
        # Row focus is not working with CheckboxTreeview
        # self.tree = ttkwidgets.CheckboxTreeview(self, columns=columns, show=['headings','tree'], selectmode='extended')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.grid(column=0, row=0, rowspan=3, sticky='nswe', **padding)

        # Buttons
        self.add_item_button = ttk.Button(self, text='Add item')
        self.add_item_button.grid(column=1, row=0, sticky='nswe', **padding)

        self.remove_item_button = ttk.Button(self, text='Remove item', command=self.delete_rows)
        self.remove_item_button.grid(column=2, row=0, sticky='nswe', **padding)

        self.move_up_button = ttk.Button(self, text='Move up', command=self.__move_row_up)
        self.move_up_button.grid(column=1, row=1, sticky='nswe', **padding)

        self.move_down_button = ttk.Button(self, text='Move down', command=self.__move_row_down)
        self.move_down_button.grid(column=2, row=1, sticky='nswe', **padding)

        self.select_button = ttk.Button(self, text='Select all')
        self.select_button.grid(column=1, row=2, sticky='nswe', **padding)

        self.deselect_button = ttk.Button(self, text='Deselect all')
        self.deselect_button.grid(column=2, row=2, sticky='nswe', **padding)

    def set_columns(self, tree_headings):
        self.tree['columns'] = tree_headings
        self.tree.column(column='#0', width=50)
        for heading in tree_headings:
            self.tree.heading(column=heading, text=heading)

    def insert_row(self, row=None):
        if row is None:
            # Ask for input
            pass
        self.tree.insert('', tk.END, values=row)

    def delete_rows(self):
        selected_rows = self.tree.selection()
        for row in selected_rows:
            self.tree.delete(row)

    def delete_all(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

    def edit_rows(self):
        selected_rows = self.tree.selection()
        for row in selected_rows:
            self.tree.item(row, tk.END, values=[])

    def __move_row_up(self):
        selected_rows = self.tree.selection()
        for row in selected_rows:
            self.tree.move(row, self.tree.parent(row), self.tree.index(row)-1)

    def __move_row_down(self):
        selected_rows = self.tree.selection()
        for row in reversed(selected_rows):
            self.tree.move(row, self.tree.parent(row), self.tree.index(row)+1)

class WelcomeFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        padding = {
            'padx': 5,
            'pady': 0
        }
        # Welcome text
        welcome_text = textwrap.dedent(
        """
        Welcome to the CV Builder app.
        This project aim to populate Jinja2 DOCX templates from resume encoded in JSON.
        You can either load an existing JSON file, or create one from scratch.
        """
        )
        self.welcome_label = ttk.Label(self,
                                       text=welcome_text)
        self.welcome_label.grid(column=0, row=0, rowspan=2, **padding)

        # Open JSON file
        self.open_json_button = ttk.Button(self,
                                           text='Open JSON file',
                                           width=20,
                                           command=self.__open_json)
        self.open_json_button.grid(column=1, row=0, sticky=tk.E, **padding)

        # Create new file
        self.edit_json_button = ttk.Button(self,
                                           width=20,
                                           text='Start from scratch')
        self.edit_json_button.grid(column=1, row=1, sticky=tk.E, **padding)

    def __open_json(self):
        file_types = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )

        json_path = filedialog.askopenfilename(
            title='Open JSON resume',
            # initialdir='/',
            filetypes=file_types
        )

        showinfo(
            title='Selected file',
            message=json_path
        )

# Resume Editor Frame
class ResumeEditorFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.__create_widgets()

    def __create_widgets(self):
        self.editor_notebook = ttk.Notebook(self)
        self.editor_notebook.pack(expand=True)

        # Page definition
        self.page_one = NotebookPersonalInfoFrame(self.editor_notebook)
        self.page_two = NotebookWorkExperienceFrame(self.editor_notebook)
        self.page_three = NotebookTrainingsFrame(self.editor_notebook)
        self.page_four = NotebookItSkillsFrame(self.editor_notebook)
        self.page_five = NotebookEducationFrame(self.editor_notebook)

        # Pack
        self.page_one.pack(fill='both', expand=True)
        self.page_two.pack(fill='both', expand=True)
        self.page_three.pack(fill='both', expand=True)
        self.page_four.pack(fill='both', expand=True)
        self.page_five.pack(fill='both', expand=True)

        # Add to notebook
        self.editor_notebook.add(self.page_one, text='Personal Information')
        self.editor_notebook.add(self.page_two, text='Work Experience')
        self.editor_notebook.add(self.page_three, text='Trainings')
        self.editor_notebook.add(self.page_four, text='IT Skills')
        self.editor_notebook.add(self.page_five, text='Education')

class NotebookPersonalInfoFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.__create_widgets()

    def __create_widgets(self):
        padding = {
            'padx': 5,
            'pady': 5
        }

        self.inputs_label_frame = ttk.LabelFrame(self, text='Contact Information')
        self.inputs_label_frame.pack(fill='both', expand=True)
        self.inputs_label_frame.columnconfigure(1, weight=1)

        # Last name
        self.last_name_label = ttk.Label(self.inputs_label_frame, text='Last name:')
        self.last_name_label.grid(column=0, row=0, sticky='w', **padding)
        self.last_name_entry = ttk.Entry(self.inputs_label_frame)
        self.last_name_entry.grid(column=1, row=0, sticky='nswe', **padding)

        # First name
        self.first_name_label = ttk.Label(self.inputs_label_frame, text='First name:')
        self.first_name_label.grid(column=0, row=1, sticky='w', **padding)
        self.first_name_entry = ttk.Entry(self.inputs_label_frame)
        self.first_name_entry.grid(column=1, row=1, sticky='nswe', **padding)

        # Position
        self.position_label = ttk.Label(self.inputs_label_frame, text='Position:')
        self.position_label.grid(column=0, row=2, sticky='w', **padding)
        self.position_entry = ttk.Entry(self.inputs_label_frame)
        self.position_entry.grid(column=1, row=2, sticky='nswe', **padding)

        # Languages
        self.languages_frame = CheckboxTreeviewFrame(self, text='Languages')
        self.languages_frame.pack(fill='both', expand=True)
        self.languages_frame.set_columns(['Language','IRL Scale','CEFR Level'])

        # Summmary
        self.summary_frame = CheckboxTreeviewFrame(self, text='Summary')
        self.summary_frame.pack(fill='both', expand=True)
        self.summary_frame.set_columns(['Description'])

        # # Sample
        languages = []
        for n in range(1,5):
            languages.append([f'language {n}',f'ilr {n}', f'cefr {n}'])

        for language in languages:
            self.languages_frame.insert_row(language)

class NotebookWorkExperienceFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.__create_widgets()

    def __create_widgets(self):
        padding = {
            'padx': 5,
            'pady': 5
        }

        works = [
            'Work A',
            'Work B'
        ]
        projects = [
            'Project AA',
            'Project AB',
            'Project BA',
            'Project BB'
        ]

        self.selection_label_frame = ttk.LabelFrame(self, text='Selection')
        self.selection_label_frame.pack(fill='both', expand=True)

        self.works_combobox = ttk.Combobox(self.selection_label_frame, values=works)
        self.works_combobox.grid(column=0, row=0, sticky='nswe', **padding)

        self.projects_combobox = ttk.Combobox(self.selection_label_frame, values=projects)
        self.projects_combobox.grid(column=0, row=1, sticky='nswe', **padding)

        # Work
        self.works_label_frame = ttk.LabelFrame(self, text='Work details')
        self.works_label_frame.pack(fill='both', expand=True)
        self.works_label_frame.columnconfigure(1, weight=1)

        # Employer
        self.work_employer_label = ttk.Label(self.works_label_frame, text='Employer:')
        self.work_employer_label.grid(column=0, row=0, sticky='w', **padding)
        self.work_employer_entry = ttk.Entry(self.works_label_frame)
        self.work_employer_entry.grid(column=1, row=0, sticky='nswe', **padding)

        # Position
        self.work_position_label = ttk.Label(self.works_label_frame, text='Position:')
        self.work_position_label.grid(column=0, row=1, sticky='w', **padding)
        self.work_position_entry = ttk.Entry(self.works_label_frame)
        self.work_position_entry.grid(column=1, row=1, sticky='nswe', **padding)

        # Starting year
        self.work_start_label = ttk.Label(self.works_label_frame, text='Starting year:')
        self.work_start_label.grid(column=0, row=2, sticky='w', **padding)
        self.work_start_spinbox = ttk.Spinbox(self.works_label_frame)
        self.work_start_spinbox.grid(column=1, row=2, sticky='nswe', **padding)

        # End year
        self.work_end_label = ttk.Label(self.works_label_frame, text='End year:')
        self.work_end_label.grid(column=0, row=3, sticky='w', **padding)
        self.work_end_spinbox = ttk.Spinbox(self.works_label_frame)
        self.work_end_spinbox.grid(column=1, row=3, sticky='nswe', **padding)

        # Work description
        self.work_description_frame = CheckboxTreeviewFrame(self, text='Work description')
        self.work_description_frame.pack(fill='both', expand=True)
        self.work_description_frame.set_columns(['Description'])

        # Project
        self.project_label_frame = ttk.LabelFrame(self, text='Project details')
        self.project_label_frame.pack(fill='both', expand=True)
        self.project_label_frame.columnconfigure(1, weight=1)

        # Name
        self.project_name_label = ttk.Label(self.project_label_frame, text='Name:')
        self.project_name_label.grid(column=0, row=0, sticky='w', **padding)
        self.project_name_entry = ttk.Entry(self.project_label_frame)
        self.project_name_entry.grid(column=1, row=0, sticky='nswe', **padding)

        # Redacted name
        self.project_redacted_label = ttk.Label(self.project_label_frame, text='Redacted name:')
        self.project_redacted_label.grid(column=0, row=0, sticky='w', **padding)
        self.project_redacted_entry = ttk.Entry(self.project_label_frame)
        self.project_redacted_entry.grid(column=1, row=0, sticky='nswe', **padding)

        # Position
        self.project_position_label = ttk.Label(self.project_label_frame, text='Position:')
        self.project_position_label.grid(column=0, row=2, sticky='w', **padding)
        self.project_position_entry = ttk.Entry(self.project_label_frame)
        self.project_position_entry.grid(column=1, row=2, sticky='nswe', **padding)

        # Starting year
        self.project_start_label = ttk.Label(self.project_label_frame, text='Starting year:')
        self.project_start_label.grid(column=0, row=3, sticky='w', **padding)
        self.project_start_spinbox = ttk.Spinbox(self.project_label_frame)
        self.project_start_spinbox.grid(column=1, row=3, sticky='nswe', **padding)

        # End year
        self.project_end_label = ttk.Label(self.project_label_frame, text='End year:')
        self.project_end_label.grid(column=0, row=4, sticky='w', **padding)
        self.project_end_spinbox = ttk.Spinbox(self.project_label_frame)
        self.project_end_spinbox.grid(column=1, row=4, sticky='nswe', **padding)

        # Project description
        self.project_description_frame = CheckboxTreeviewFrame(self, text='Project description')
        self.project_description_frame.pack(fill='both', expand=True)
        self.project_description_frame.set_columns(['Description'])

        # Project activities
        self.project_description_frame = CheckboxTreeviewFrame(self, text='Project activities')
        self.project_description_frame.pack(fill='both', expand=True)
        self.project_description_frame.set_columns(['Activity'])

class NotebookTrainingsFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.__create_widgets()

    def __create_widgets(self):
        self.trainings_frame = CheckboxTreeviewFrame(self)
        self.trainings_frame.pack(fill='both', expand=True)
        self.trainings_frame.set_columns(['Description'])

class NotebookItSkillsFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.__create_widgets()

    def __create_widgets(self):
        self.itskills_frame = CheckboxTreeviewFrame(self)
        self.itskills_frame.pack(fill='both', expand=True)
        self.itskills_frame.set_columns(['Description'])

class NotebookEducationFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.__create_widgets()

    def __create_widgets(self):
        self.educations_frame = CheckboxTreeviewFrame(self)
        self.educations_frame.pack(fill='both', expand=True)
        self.educations_frame.set_columns(['School','Degree','Starting year','Ending year'])

# Application Window
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window
        self.title('CV Builder')
        # self.geometry('600x600')
        # self.resizable(0, 0)
        self.style = ttk.Style(self)

        self.__create_widgets()

    def __create_widgets(self):
        # welcome_frame = WelcomeFrame(self)
        # welcome_frame.grid(column=0, row=0)

        editor_frame = ResumeEditorFrame(self)
        # editor_frame.grid(column=0, row=0)
        editor_frame.pack(fill='both', expand=True)

# Main execution
if __name__ == "__main__":
    app = App()
    app.mainloop()