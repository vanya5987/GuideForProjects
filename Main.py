from Data.DataManager import DataManager

#controls
from Controls.TableView import TableView
from Controls.ControlPanel import ControlPanel
#controls

#lib_modules
import tkinter as tk
#lib_modules

class Main:
    def __init__(self):
        root: tk.Tk = tk.Tk()
        root.title("Test V2")
        dataManager: DataManager = DataManager()
        tableView: TableView = TableView(root, dataManager)
        tableView.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        controlPanel: ControlPanel = ControlPanel(root, tableView, dataManager)
        controlPanel.pack(side=tk.RIGHT, fill=tk.Y)

        root.mainloop()

main: Main = Main()