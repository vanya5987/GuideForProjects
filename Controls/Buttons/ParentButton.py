#lib_modules
from typing import *
from tkinter import ttk
import tkinter as tk
#lib_modules

class ParentButton:
    def __init__(self, master: tk.Tk):
        self.master: tk.Tk = master

    def CreateButton(self, text: str, command: Callable, style: str) -> ttk.Button:
        return ttk.Button(self.master, text=text, command=command, style=style)

    def SetButtonPosition(self, positionY: int, button: ttk.Button) -> None:
        button.pack(pady=positionY)