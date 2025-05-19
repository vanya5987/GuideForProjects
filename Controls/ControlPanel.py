#containers
from Containers.TextContainer import TextContainer
from Containers.StyleContainer import StyleContainer
#containers

#buttons_group
from Controls.Buttons.ParentButton  import ParentButton
from Controls.Buttons.DeleteRowButton import DeleteRowButton
from Controls.Buttons.AddedRowButton import AddedRowButton
#buttons_group

#controls_group
from Controls.RadioButtons.RadioButton import RadioButton
from Controls.Entrys.Entrys import Entrys
from Controls.LabelFrames.RadioFrame import RadioFrame
from Controls.TableView import TableView
#controls_group

from Style.WidgetStyleConfig import WidgetStyleConfig
from Data.DataManager import DataManager

#lib_modules
from tkinter import ttk
import tkinter as tk
#lib_modules

class ControlPanel(ttk.Frame): #Эта панель - обьект который будет создаваться и размещать на себе сразу все контролы для этой панели.
    def __init__(self, master: tk.Tk, tableView: TableView, dataManager: DataManager):

#containers_initialization
        textContainer: TextContainer = TextContainer()
        styleContainer: StyleContainer = StyleContainer()
#containers_initialization

        widgetStyle: WidgetStyleConfig = WidgetStyleConfig()

#buttons_initialize_object
        parrentButton: ParentButton = ParentButton(master)
        deleteButton: DeleteRowButton = DeleteRowButton(parrentButton, tableView, dataManager)
        addButton: AddedRowButton = AddedRowButton(parrentButton, tableView, dataManager)
#buttons_initialize_object

        radioVar: tk.StringVar = tk.StringVar(value=textContainer.controlPanelText[0])
        entrys: Entrys = Entrys(master)

#radio_initiazile_group
        radioButton: RadioButton = RadioButton(radioVar)
        self.radioFrame: RadioFrame = RadioFrame(master)
#radio_initiazile_group

        controlPanelPadding: int = 10

        super().__init__(master, style=styleContainer.controlPannelStyle)
        self.configure(padding=controlPanelPadding)

        radioFrame: ttk.Labelframe = self.radioFrame.CreateRadioFrame()
        
#create_radio_buttons
        radioButton.CreateRadioButton(radioFrame, textContainer.controlPanelText[0])
        radioButton.CreateRadioButton(radioFrame, textContainer.controlPanelText[1])
#create_radio_buttons

        entryA2: ttk.Entry = entrys.CreateEntryA2()
        widgetStyle.CreateBasePanelStyle()

#create_buttons
        addButton.CreateAddButton(entryA2, radioVar)
        deleteButton.CreateDeleteButton()
#create_buttons