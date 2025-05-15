import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

# Цветовая схема
BACKGROUND_COLOR = "#C0C0C0"
TEXT_COLOR = "#333333"      ## Черный
ACCENT_COLOR = "#C0C0C0"    #### Остальные цвета серый.
HIGHLIGHT_COLOR = "#C0C0C0"
BUTTON_TEXT_COLOR = "#C0C0C0"

class DataManager:
    def __init__(self, filepath="table_data.json"): #
        self.filepath = os.path.abspath(filepath) # Путь к файлу

    def load_data(self): # Загрузка данных
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError): # Обработка ошибок при загрузке
            return []

    def save_data(self, data): # Сохранение данных в файл
        try:
            with open(self.filepath, "w") as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка сохранения данных: {e}") # Выводим сообщение об ошибке
            return False


class TableView(ttk.Frame):
    def __init__(self, master, data_manager):
        super().__init__(master, style="TFrame")
        self.data_manager = data_manager
        self.table_data = data_manager.load_data()

        style = ttk.Style()
        style.configure("Treeview", background=BACKGROUND_COLOR, foreground=TEXT_COLOR,
                        fieldbackground=BACKGROUND_COLOR, borderwidth=1, highlightthickness=0)
        style.configure("Treeview.Heading", background="#e0e0e0", foreground=TEXT_COLOR, font=("Helvetica", 10, "bold"))
        style.map("Treeview", background=[("selected", HIGHLIGHT_COLOR)])

        self.tree = ttk.Treeview(self, columns=("Column1", "Column2"), show="headings", style="Treeview")
        self.tree.heading("Column1", text="Текст записи")
        self.tree.heading("Column2", text="Выбор переключателя")
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.update_table()

    def update_table(self): # Обновление отображения таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in self.table_data:
            self.tree.insert("", tk.END, values=row)

    def add_row(self, entry_text, radio_choice): # Добавление новой строки
        self.table_data.append([entry_text, radio_choice])
        self.update_table()
        return self.data_manager.save_data(self.table_data)

    def delete_selected(self):
        selected_items = self.tree.selection()
        if selected_items:
            for item in reversed(selected_items):
                self.table_data.pop(self.tree.index(item))
                self.tree.delete(item)
            self.data_manager.save_data(self.table_data)
            self.update_table()


class ControlPanel(ttk.Frame):
    def __init__(self, master, table_view):
        super().__init__(master, style="ControlPanel.TFrame")
        self.table_view = table_view
        self.configure(padding=10)

        self.radio_var = tk.StringVar(value="Вариант А")
        radio_frame = ttk.Labelframe(self, text="Выбор", style="TLabelframe")
        radio_frame.pack(pady=10)

        ttk.Radiobutton(radio_frame, text="Вариант А", variable=self.radio_var, value="Вариант А", style="TRadiobutton").pack(anchor=tk.W, padx=5, pady=5)
        ttk.Radiobutton(radio_frame, text="Вариант Б", variable=self.radio_var, value="Вариант Б", style="TRadiobutton").pack(anchor=tk.W, padx=5, pady=5)

        self.entry_a2 = ttk.Entry(self, style="TEntry")
        self.entry_a2.pack(pady=10)

        style = ttk.Style()
        style.configure("ControlPanel.TFrame", background=BACKGROUND_COLOR)
        style.configure("Accent.TButton", background=ACCENT_COLOR, foreground=BUTTON_TEXT_COLOR, padding=10,
                        font=("Helvetica", 12, "bold"))
        add_button = ttk.Button(self, text="Добавить", command=self.add_data, style="Accent.TButton")
        add_button.pack(pady=5)
        delete_button = ttk.Button(self, text="Удалить", command=self.table_view.delete_selected,
                                   style="Accent.TButton")
        delete_button.pack(pady=5)

    def add_data(self):  # Добавление данных в таблицу
        entry_text = self.entry_a2.get()
        radio_choice = self.radio_var.get()
        if entry_text:  # Проверка на пустую строку
            self.table_view.add_row(entry_text, radio_choice)
            self.entry_a2.delete(0, tk.END)  # Очищаем поле ввода


root = tk.Tk()
root.title("Test V2")
data_manager = DataManager()
table_view = TableView(root, data_manager)
table_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
control_panel = ControlPanel(root, table_view)
control_panel.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()