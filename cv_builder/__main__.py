# -*- coding: utf-8 -*-
"""Main execution of the 'cv_builder' project."""

__version__ = "0.5.0"

import tkinter as tk
from tkinter import ttk

from cv_builder.app import ControlFrame


class App(tk.Tk):
    """App: inherit from 'tkinter.Tk'."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the App class instance."""
        super().__init__(*args, **kwargs)

        self.title("CV Builder")
        self.style = ttk.Style(self)

        self.control_frame = ControlFrame(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
