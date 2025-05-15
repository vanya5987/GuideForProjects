from Containers.StyleContainer import StyleContainer

#lib_modules
from tkinter import ttk
import tkinter as tk
#lib_modules

class Entrys:
    def __init__(self, master: tk.Tk):
        self.master: tk.Tk = master

        self.styleContainers: StyleContainer = StyleContainer()

        self.positionY: int = 10

    def CreateEntryA2(self) -> ttk.Entry:
        entryA2: ttk.Entry = ttk.Entry(self.master, style=self.styleContainers.entrysStyle)
        entryA2.pack(pady=self.positionY)

        return entryA2