# -* coding: utf-8 -*-
"""
main.py contains the main back-end flow and GUI of the cv_builder project.
"""
# Import libraries
from docxtpl import DocxTemplate
# from template_pptx_jinja.render import PPTXRendering
# from pptx_template import render
# from pptx_templater.core import convert
import jinja2
import textwrap
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from classes import load_employee_json

# Project List frame
class ProjectsListFrame(ttk.LabelFrame):
    def __init__(self, container, work_index, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container
        self.work_index = work_index
        self.work_experience = self.container.employee.works[self.work_index]

        self.__create_widgets()
        self.grid(column=0, row=0, sticky='nswe')

    def __create_widgets(self):
        self['text'] = self.work_experience.employer

        self.information_label = tk.Label(self,
                                          text="Please select for which projects you want to display the client name")
        self.information_label.grid(sticky='w')

        self.check_vars = {}
        self.check_buttons = {}
        for project_index, project in enumerate(self.work_experience.projects):
            if project.name is not None:
                self.check_vars[project_index] = tk.BooleanVar()
                self.check_buttons[project_index] = tk.Checkbutton(self,
                                                                   text=f"{project.name}: {project.position} ({project.start})",
                                                                   command=self.__update_confidential_status,
                                                                   variable=self.check_vars[project_index],
                                                                   onvalue=True,
                                                                   offvalue=False)
                self.check_buttons[project_index].grid(sticky='w')

    def __update_confidential_status(self):
        # BUG: Doesn't update if trying to build a second time
        #      Probably due to the re-ordering
        #      Need to use different indexes?
        for project_index in self.check_vars:
            self.container.employee.works[self.work_index].projects[project_index].confidential = not self.check_vars[project_index].get()

# Main frame
class LoadFilesFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container

        self.__create_widgets()
        self.grid(column=0, row=0, sticky='nswe')

    def __create_widgets(self):
        padding = {
            'padx': 5,
            'pady': 5
        }

        # Welcome text
        welcome_text = textwrap.dedent(
        """
        Welcome to the CV Builder app.
        This project aim to populate Jinja2 DOCX and PPTX templates from resume encoded in JSON.
        """
        )
        self.welcome_label = ttk.Label(self,
                                       text=welcome_text)
        self.welcome_label.pack(fill='both', expand=True, **padding)

        # File selection frame
        self.file_loading_frame = ttk.LabelFrame(self, text='File loading')
        self.file_loading_frame.pack(fill='both', expand=True)
        self.file_loading_frame.columnconfigure(1, weight=1)

        # Select JSON
        self.json_button = ttk.Button(self.file_loading_frame,
                                      text='Select JSON resume',
                                      width=20,
                                      command=self.__open_json)
        self.json_button.grid(column=0, row=0, sticky='w', **padding)
        self.json_label = ttk.Label(self.file_loading_frame, text='No file loaded.')
        self.json_label.grid(column=1, row=0, sticky='nswe', **padding)

        # Select DOCX
        self.docx_button = ttk.Button(self.file_loading_frame,
                                      text='Select DOCX template',
                                      width=20,
                                      command=self.__open_docx)
        self.docx_button.grid(column=0, row=1, sticky='w', **padding)
        self.docx_label = ttk.Label(self.file_loading_frame, text='No file loaded.')
        self.docx_label.grid(column=1, row=1, sticky='nswe', **padding)

        # Select PPTX
        self.pptx_button = ttk.Button(self.file_loading_frame,
                                      text='Select PPTX template',
                                      width=20,
                                      command=self.__open_pptx)
        self.pptx_button.grid(column=0, row=2, sticky='w', **padding)
        self.pptx_label = ttk.Label(self.file_loading_frame, text='No file loaded.')
        self.pptx_label.grid(column=1, row=2, sticky='nswe', **padding)

        # TODO: Activate the button once the PPTX function will work
        self.pptx_button.state(['disabled'])

    def __reset_project_frames(self):
        while len(self.container.control_frame.frames) != 1:
            self.container.control_frame.frames.pop(-1)

        for work_index, work in enumerate(self.container.employee.works):
            if not any(project.name is None for project in work.projects):
                self.container.control_frame.frames.append(
                    ProjectsListFrame(self.container, work_index=work_index)
                )

        self.container.control_frame.frames[0].tkraise()

    def __open_json(self):
        file_types = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )

        self.json_path = filedialog.askopenfilename(
            title='Open JSON resume',
            filetypes=file_types
        )

        try:
            self.container.employee = load_employee_json(self.json_path, 'utf-8')
            self.json_label['text'] = self.json_path
            self.container.control_frame.next_button.state(['!disabled'])
            self.__reset_project_frames()
        except Exception as err:
            showerror(
                title='Error',
                message=f'Unable to load JSON file:\n{err}'
            )

    def __open_docx(self):
        file_types = (
            ('docx files', '*.docx'),
            ('All files', '*.*')
        )

        self.docx_path = filedialog.askopenfilename(
            title='Open DOCX template',
            filetypes=file_types
        )

        try:
            self.docx_tpl = DocxTemplate(self.docx_path)
            self.docx_label['text'] = self.docx_path
            self.container.control_frame.build_docx_button.state(['!disabled'])
        except Exception as err:
            showerror(
                title='Error',
                message=f'Unable to load DOCX file:\n{err}'
            )

    def __open_pptx(self):
        file_types = (
            ('pptx files', '*.pptx'),
            ('All files', '*.*')
        )

        self.pptx_path = filedialog.askopenfilename(
            title='Open PPTX template',
            filetypes=file_types
        )

        try:
            # self.pptx_tpl = DocxTemplate(self.pptx_path)
            self.pptx_label['text'] = self.pptx_path
            self.container.control_frame.build_pptx_button.state(['!disabled'])
        except Exception as err:
            showerror(
                title='Error',
                message=f'Unable to load PPTX file:\n{err}'
            )

    @staticmethod
    def __ask_save_path(file_type=None):
        if file_type == 'docx':
            file_types = (
                ('docx files', '*.docx'),
                ('All files', '*.*')
            )
        elif file_type == 'pptx':
            file_types = (
                ('pptx files', '*.pptx'),
                ('All files', '*.*')
            )
        else:
            file_types = (
                ('docx files', '*.docx'),
                ('pptx files', '*.pptx'),
                ('All files', '*.*')
            )

        save_path = filedialog.asksaveasfilename(
            title='Save as',
            filetypes=file_types
        )

        return save_path

    @staticmethod
    def __format_date(date_int):
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

    def build_docx_template(self):
        # Get save path
        save_path = self.__ask_save_path('docx')

        # Sort by descending
        self.container.employee.sort_works("desc")
        self.container.employee.sort_projects("desc")
        self.container.employee.sort_educations("desc")

        # Load Jinja env
        jinja_env = jinja2.Environment()
        jinja_env.filters['format_date'] = self.__format_date

        # Set context
        context = self.container.employee.to_dict(keep_none=False)

        # Export
        try:
            self.docx_tpl.render(context, jinja_env=jinja_env, autoescape=True)
            self.docx_tpl.save(save_path)

            # Confirmation message
            showinfo(
                title='Generated resume',
                message=f'Resume saved under\n{save_path}'
            )
        except Exception as err:
            showerror(
                title='Error',
                message=f'Unable to build the DOCX template:\n{err}'
            )

    def build_pptx_template(self):
        # BUG:
        # * template_pptx_jinja not working: error
        # * pptx_template not working: no error but just a copy of the template
        # * pptx_templater not working: should convert string to json?

        # Get save path
        save_path = self.__ask_save_path('pptx')

        # Sort by descending
        self.container.employee.sort_works("desc")
        self.container.employee.sort_projects("desc")
        self.container.employee.sort_educations("desc")

        # Load Jinja env
        jinja_env = jinja2.Environment()

        # Set context
        # model = self.container.employee.to_dict(keep_none=False)
        model = {
            'lastname': 'Doe',
            'firstname': 'John',
            'position': 'Consultant'
        }

        data = {
            'model': model
        }

        j = {
            'slides': [
                {
                    'layoutSlideNum': 0,
                    'text': {
                    'lastname': 'Doe',
                    'firstname': 'John',
                    'position': 'Consultant'
                    }
                }
            ]
        }

        # data = {
        #     'slides': [
        #         {
        #             'layoutSlideNum': 0,
        #             'text': model
        #         }
        #     ]
        # }

        # Export
        # try:
        # rendering = PPTXRendering(self.pptx_path, data, save_path, jinja_env)
        # message = rendering.process()
        # showinfo(
        #     title='Generated resume',
        #     message=message
        # )
        # render.render_pptx(self.pptx_path, model, save_path)
        convert(self.pptx_path, j, save_path)
        # except Exception as err:
        #     showerror(
        #         title='Error',
        #         message=f'Unable to build PPTX template:\n{err}'
        #     )

# Control frame
class ControlFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container

        self.__create_widgets()
        self.grid(column=0, row=1)

    def __create_widgets(self):
        padding = {
            'padx': 5,
            'pady': 5
        }

        self.previous_button = ttk.Button(self,
                                          text='Previous',
                                          command=self.__previous_frame)
        self.previous_button.grid(column=2, row=1, **padding)

        self.next_button = ttk.Button(self,
                                      text='Next',
                                      command=self.__next_frame)
        self.next_button.grid(column=3, row=1, **padding)

        # Initialize frames
        self.frames = []
        self.frames.append(LoadFilesFrame(self.container))

        # Build DOCX
        self.build_docx_button = ttk.Button(self,
                                            text='Build DOCX resume',
                                            command=self.frames[0].build_docx_template)
        self.build_docx_button.grid(column=0, row=1, **padding)

        # Build PPTX
        self.build_pptx_button = ttk.Button(self,
                                            text='Build PPTX resume',
                                            command=self.frames[0].build_pptx_template)
        self.build_pptx_button.grid(column=1, row=1, **padding)

        # Display default
        self.current_frame = 0
        self.__change_frame(self.current_frame)

        # Set states
        self.previous_button.state(['disabled'])
        self.next_button.state(['disabled'])
        self.build_docx_button.state(['disabled'])
        self.build_pptx_button.state(['disabled'])

    def __change_frame(self, frame_pos):
        # Toggle button states
        if frame_pos == 0:
            self.previous_button.state(['disabled'])
            self.next_button.state(['!disabled'])
        elif frame_pos == len(self.frames) - 1:
            self.previous_button.state(['!disabled'])
            self.next_button.state(['disabled'])
        else:
            self.previous_button.state(['!disabled'])
            self.next_button.state(['!disabled'])

        # Change frame
        self.frames[frame_pos].tkraise()

    def __next_frame(self):
        self.current_frame += 1
        self.__change_frame(self.current_frame)

    def __previous_frame(self):
        self.current_frame -= 1
        self.__change_frame(self.current_frame)

# App
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('CV Builder')
        self.style = ttk.Style(self)

        self.control_frame = ControlFrame(self)

# Run app
if __name__ == "__main__":
    app = App()
    app.mainloop()
