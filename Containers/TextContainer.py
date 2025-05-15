from typing import *

class TextContainer:
    def __init__(self):
        self.addButtonText: str = "Добавить"
        self.deleteButtonText: str = "Удалить"
        self.radioFrameText: str = "Выбор"

        self.tableViewText: Dict[int, str] = {0: "Текст записи", 1: "Выбор переключателя"}
        self.controlPanelText: Dict[int, str] = {0: "Вариант А", 1: "Вариант Б"}