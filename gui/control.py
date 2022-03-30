# -* coding: utf-8 -*-
"""
control.py
Author: Gilson, K
"""

from tkinter import ttk

from .load_files import LoadFilesFrame


class ControlFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.container = container

        self.__create_widgets()
        self.grid(column=0, row=1)

    def __create_widgets(self):
        padding = {"padx": 5, "pady": 5}

        self.previous_button = ttk.Button(
            self, text="Previous", command=self.__previous_frame
        )
        self.previous_button.grid(column=2, row=1, **padding)

        self.next_button = ttk.Button(self, text="Next", command=self.__next_frame)
        self.next_button.grid(column=3, row=1, **padding)

        # Initialize frames
        self.frames = []
        self.frames.append(LoadFilesFrame(self.container))

        # Build DOCX
        self.build_docx_button = ttk.Button(
            self, text="Build DOCX resume", command=self.frames[0].build_docx_template
        )
        self.build_docx_button.grid(column=0, row=1, **padding)

        # Build PPTX
        self.build_pptx_button = ttk.Button(
            self, text="Build PPTX resume", command=self.frames[0].build_pptx_template
        )
        self.build_pptx_button.grid(column=1, row=1, **padding)

        # Display default
        self.current_frame = 0
        self.__change_frame(self.current_frame)

        # Set states
        self.previous_button.state(["disabled"])
        self.next_button.state(["disabled"])
        self.build_docx_button.state(["disabled"])
        self.build_pptx_button.state(["disabled"])

    def __change_frame(self, frame_pos):
        # Toggle button states
        if frame_pos == 0:
            self.previous_button.state(["disabled"])
            self.next_button.state(["!disabled"])
        elif frame_pos == len(self.frames) - 1:
            self.previous_button.state(["!disabled"])
            self.next_button.state(["disabled"])
        else:
            self.previous_button.state(["!disabled"])
            self.next_button.state(["!disabled"])

        # Change frame
        self.frames[frame_pos].tkraise()

    def __next_frame(self):
        self.current_frame += 1
        self.__change_frame(self.current_frame)

    def __previous_frame(self):
        self.current_frame -= 1
        self.__change_frame(self.current_frame)
