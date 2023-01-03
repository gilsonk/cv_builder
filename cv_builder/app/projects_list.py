# -*- coding: utf-8 -*-
"""The 'project_list' module of the 'app' package contains frames related to listing Project objects."""

import tkinter as tk
from tkinter import ttk
from typing import Any


class ProjectsListFrame(ttk.LabelFrame):
    """Projects Listing Frame.

    This frame holds the actions related to listing and toogling Project objects.

    Parameters
    ----------
    container : Any
        The parent widget.
    work_index : int
        The index of the WorkExperience to display.
    """

    def __init__(self, container: Any, work_index: int, *args, **kwargs) -> None:
        """Initialise the ProjectsListFrame class instance."""
        super().__init__(container, *args, **kwargs)
        self.container = container
        self.work_index = work_index
        self.work_experience = self.container.employee.works[self.work_index]

        self.__create_widgets()
        self.grid(column=0, row=0, sticky="nswe")

    def __create_widgets(self) -> None:
        """Initialise the widgets within the frame."""
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

    def __update_confidential_status(self) -> None:
        """Update the confidential status of the projects for the given WorkExperience."""
        # FIXME: Doesn't update if trying to build a second time
        #        Probably due to the re-ordering
        #        Need to use different indexes?
        for project_index in self.check_vars:
            self.container.employee.works[self.work_index].projects[
                project_index
            ].confidential = not self.check_vars[project_index].get()
