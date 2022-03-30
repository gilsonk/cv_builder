# -* coding: utf-8 -*-
"""
project_list.py
Author: Gilson, K
"""

import tkinter as tk
from tkinter import ttk


class ProjectsListFrame(ttk.LabelFrame):
    def __init__(self, container, work_index, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container
        self.work_index = work_index
        self.work_experience = self.container.employee.works[self.work_index]

        self.__create_widgets()
        self.grid(column=0, row=0, sticky="nswe")

    def __create_widgets(self):
        self["text"] = self.work_experience.employer

        self.information_label = tk.Label(
            self,
            text="Please select for which projects you want to display the client name",
        )
        self.information_label.grid(sticky="w")

        self.check_vars = {}
        self.check_buttons = {}
        for project_index, project in enumerate(self.work_experience.projects):
            if project.name is not None:
                self.check_vars[project_index] = tk.BooleanVar()
                self.check_buttons[project_index] = tk.Checkbutton(
                    self,
                    text=f"{project.name}: {project.position} ({project.start})",
                    command=self.__update_confidential_status,
                    variable=self.check_vars[project_index],
                    onvalue=True,
                    offvalue=False,
                )
                self.check_buttons[project_index].grid(sticky="w")

    def __update_confidential_status(self):
        # BUG: Doesn't update if trying to build a second time
        #      Probably due to the re-ordering
        #      Need to use different indexes?
        for project_index in self.check_vars:
            self.container.employee.works[self.work_index].projects[
                project_index
            ].confidential = not self.check_vars[project_index].get()
