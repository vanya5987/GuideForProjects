from Containers.StyleContainer import StyleContainer

#lib_modules
from tkinter import ttk
import tkinter as tk
#lib_modules

class RadioButton:
    def __init__(self, radioVar: tk.StringVar):
        self.radioVar: tk.StringVar = radioVar

        self.styleContainer: StyleContainer = StyleContainer()

        self.positionX = 5
        self.positionY = 5

    def CreateRadioButton(self, radioFrame: ttk.Labelframe, text: str) -> ttk.Radiobutton:
        return ttk.Radiobutton(radioFrame, text=text, variable= self.radioVar, value=text,
                                style=self.styleContainer.radioButtonStyle).pack(anchor=tk.W, padx=self.positionX, pady=self.positionY)