#create_controls
from Controls.Buttons.ParentButton import ParentButton
from Controls.TableView import TableView
#create_controls

from Data.DataManager import DataManager

#containers
from Containers.TextContainer import TextContainer
from Containers.StyleContainer import StyleContainer
#containers

#lib_modules
from typing import *
from tkinter import ttk
import tkinter as tk
#lib_modules

class AddedRowButton:
    def __init__(self, parrentButton: ParentButton, tableView: TableView, dataManager: DataManager):
        self.parrentButton: ParentButton = parrentButton
        self.tableView: TableView = tableView
        self.dataManager: DataManager = dataManager

#containers_initialization
        self.textContainer: TextContainer = TextContainer()
        self.styleContainer: StyleContainer = StyleContainer()
#containers_initialization

        self.buttonPositionY: int = 5
    
    def CreateAddButton(self, entryA2: ttk.Entry, radioVar: tk.StringVar) -> None:
        deleteButton: ttk.Button = self.parrentButton.CreateButton(self.textContainer.addButtonText, lambda: self.AddData(entryA2, radioVar), self.styleContainer.addedRowButtonStyle)
        self.parrentButton.SetButtonPosition(self.buttonPositionY, deleteButton)

    def AddData(self, entryA2: ttk.Entry, radioVar: tk.StringVar):  # Добавление данных в таблицу
        entryText: str = entryA2.get()
        radioChoice: str = radioVar.get()
        
        if entryText:  # Проверка на пустую строку
            self.AddRow(entryText, radioChoice, self.tableView.tableData)
            entryA2.delete(0, tk.END)  # Очищаем поле ввода

    def AddRow(self, entryText: str, radioChoice: str, tableData: List[str]): # Добавление новой строки
        tableData.append([entryText, radioChoice])
        self.tableView.UpdateTable()
        return self.dataManager.SaveData(tableData)
