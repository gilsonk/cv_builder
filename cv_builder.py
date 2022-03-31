# -* coding: utf-8 -*-
"""
cv_builder.py
Author: Gilson, K
"""

__version__ = "0.5.0"

import tkinter as tk
from tkinter import ttk

import gui


class App(tk.Tk):
    """App: inherit from 'tkinter.Tk'."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the App class instance."""
        super().__init__(*args, **kwargs)

        self.title("CV Builder")
        self.style = ttk.Style(self)

        self.control_frame = gui.ControlFrame(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
