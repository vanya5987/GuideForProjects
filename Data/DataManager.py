#lib_modules
from tkinter import messagebox
from typing import *
import json
import os
#lib_modules

class DataManager:
    def __init__(self):
        self.filepath = os.path.abspath("table_data.json") #Путь к файлу.

#Загрузка данных в json-файл.
    def LoadData(self) -> List[str]:
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError): #Обработка ошибок при загрузке.
            return []

#Сохранение данных в json-файл.
    def SaveData(self, data: List[str]) -> bool:
        try:
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка сохранения данных: {e}") #Выводим сообщение об ошибке.
            return False