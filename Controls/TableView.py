#containers
from Containers.ColorsContainer import ColorsContainer
from Containers.TextContainer import TextContainer
from Containers.StyleContainer import StyleContainer
#containers

from Style.WidgetStyleConfig import WidgetStyleConfig
from Data.DataManager import DataManager

#lib_modules
from typing import *
from tkinter import ttk
import tkinter as tk
#lib_modules

class TableView(ttk.Frame):
    def __init__(self, master, dataManager: DataManager):
#containers_initialize
        self.colorsContainer: ColorsContainer = ColorsContainer()
        self.textContainer: TextContainer = TextContainer()
        self.styleContainer: StyleContainer = StyleContainer()
#containers_initialize

        self.widgetStyle: WidgetStyleConfig = WidgetStyleConfig()

        super().__init__(master, style="TFrame")
        self.tableData: List[str] = dataManager.LoadData()

        self.widgetStyle.CreateTableViewStyle()
        self.CreateTree()
        self.UpdateTable()

    def UpdateTable(self): # Обновление отображения таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in self.tableData:
            self.tree.insert("", tk.END, values=row)

    def CreateTree(self):
        self.tree = ttk.Treeview(self, columns=("Column1", "Column2"), show="headings", style=self.styleContainer.treeStyle)
        self.tree.heading("Column1", text=self.textContainer.tableViewText[0])
        self.tree.heading("Column2", text=self.textContainer.tableViewText[1])
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.UpdateTable()