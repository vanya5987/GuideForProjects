#containers
from Containers.ColorsContainer import ColorsContainer
from Containers.StyleContainer import StyleContainer
from Containers.FontStyleContainer import FontStyleContainer
#containers

#lib_modules
from tkinter import ttk
#lib_modules

class WidgetStyleConfig:
    def __init__(self):
#containers_initialization
        self.colorsContainer: ColorsContainer = ColorsContainer()
        self.styleContainer: StyleContainer = StyleContainer()
        self.fontStyleContainer: FontStyleContainer = FontStyleContainer()
#containers_initialization

        self.position: int = 10
        self.basePanelFontSize: int = 12
        self.tableViewFontSize: int = 10

    def CreateBasePanelStyle(self) -> None:
        style: ttk.Style = ttk.Style()
        style.configure(self.styleContainer.controlPannelStyle, background=self.colorsContainer.backgroundColor)
        style.configure(self.styleContainer.widgetStyleButton, background=self.colorsContainer.accentColor, foreground=self.colorsContainer.buttonTextCollor, padding=self.position,
                        font=(self.fontStyleContainer.widgetFontStyle, self.basePanelFontSize, "bold"))
        
    def CreateTableViewStyle(self) -> None:
        style = ttk.Style()
        style.configure(self.styleContainer.treeStyle, background=self.colorsContainer.backgroundColor, foreground=self.colorsContainer.textColor,
                        fieldbackground=self.colorsContainer.backgroundColor, borderwidth=1, highlightthickness=0)
        style.configure(self.styleContainer.treevievStyle, background=self.colorsContainer.treeBackgroundColor, foreground=self.colorsContainer.textColor,
                         font=(self.fontStyleContainer.widgetFontStyle, self.tableViewFontSize, "bold"))
        style.map(self.styleContainer.treeStyle, background=[("selected", self.colorsContainer.highlightColor)])