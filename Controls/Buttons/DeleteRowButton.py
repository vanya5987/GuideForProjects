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
#lib_modules

class DeleteRowButton:
    def __init__(self, parrentButton: ParentButton, tableView: TableView, dataManager: DataManager):
        self.parrentButton: ParentButton = parrentButton
        self.tableView: TableView = tableView
        self.dataManager: DataManager = dataManager

#containers_initialization
        self.textContainer: TextContainer = TextContainer()
        self.styleContainer: StyleContainer = StyleContainer()
#containers_initialization

        self.buttonPositionY: int = 5
    
    def CreateDeleteButton(self) -> None:
        deleteButton: ttk.Button = self.parrentButton.CreateButton(self.textContainer.deleteButtonText, self.DeleteSelected, self.styleContainer.deletedRowButtonStyle)
        self.parrentButton.SetButtonPosition(self.buttonPositionY, deleteButton)

    def DeleteSelected(self):
        selectedItems: Tuple[str, any] = self.tableView.tree.selection()
        if selectedItems:
            for item in reversed(selectedItems):
                self.tableView.tableData.pop(self.tableView.tree.index(item))
                self.tableView.tree.delete(item)
            self.dataManager.SaveData(self.tableView.tableData)
            self.tableView.UpdateTable()
