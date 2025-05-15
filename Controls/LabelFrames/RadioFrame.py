#containers
from Containers.TextContainer import TextContainer
from Containers.StyleContainer import StyleContainer
#containers

#lib_modules
from tkinter import ttk
import tkinter as tk
#lib_modules

class RadioFrame:
    def __init__(self, master: tk.Tk):
        self.master: tk.Tk = master

#containers_initialization
        self.textContainer: TextContainer = TextContainer()
        self.styleContainers: StyleContainer = StyleContainer()
#containers_initialization

        self.positionY: int = 10
        
    def CreateRadioFrame(self) -> None:
        radioFrame: ttk.Labelframe = ttk.Labelframe(self.master, text=self.textContainer.radioFrameText, style=self.styleContainers.radioFrameStyle)
        radioFrame.pack(pady=self.positionY)