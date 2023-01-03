# -*- coding: utf-8 -*-
"""The 'control' module of the 'app' package contains the main Tkinter control frame."""

from tkinter import ttk
from typing import Any

from cv_builder.app.load_files import LoadFilesFrame


class ControlFrame(ttk.Frame):
    """Main Control Frame.

    This frame holds the main buttons and widget of the interface.

    Parameters
    ----------
    container : Any
        The parent widget.
    """

    def __init__(self, container: Any, *args, **kwargs) -> None:
        """Initialise the ControlFrame class instance."""
        super().__init__(container, *args, **kwargs)
        self.container = container

        self.__create_widgets()
        self.grid(column=0, row=1)

    def __create_widgets(self) -> None:
        """Initialise widgets within the frame."""
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

    def __change_frame(self, frame_pos: int) -> None:
        """Move between frames.

        Parameters
        ----------
        frame_pos : int
            The position of the frame to go to.
        """
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

    def __next_frame(self) -> None:
        """Move to the next frame."""
        self.current_frame += 1
        self.__change_frame(self.current_frame)

    def __previous_frame(self) -> None:
        """Move to the previous frame."""
        self.current_frame -= 1
        self.__change_frame(self.current_frame)
