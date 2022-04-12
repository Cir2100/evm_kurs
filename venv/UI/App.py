import tkinter as tk
from tkinter import messagebox
from screeninfo import get_monitors

from UI.BacroundCanvas import BacgroundCanvas
from UI.TableView import TableView
from data.Elements import elements
from data.calcylate import calcylate
import data.screenshot as screenshot

from data.fabric import create_element

from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Рисуем вторую лабу")
        monitor = get_monitors()[0]
        #self.geometry(f"{monitor.width}x{monitor.height}+0+0")
        self.geometry(f"{800}x{600}+0+0")
        self.bacgroung = BacgroundCanvas(self)
        self.create_menu()
        self.create_theme_table_view()
        self.mainloop()

    def create_menu(self):
        add_menu = tk.Menu(master=self)

        add_menu.add_command(label="Мультиплексор", command=lambda: elements.
                             add_element(create_element("MS", self.bacgroung)))
        add_menu.add_command(label="Дешифратор", command=lambda:elements.
                             add_element(create_element("DC", self.bacgroung)))
        add_menu.add_command(label="Шифратор", command=lambda:elements.
                             add_element(create_element("CD", self.bacgroung)))
        add_menu.add_command(label="Не", command=lambda:elements.
                             add_element(create_element("NO", self.bacgroung)))
        add_menu.add_command(label="Выход", command=self.add_out)
        main_menu = tk.Menu(master=self, tearoff=0)
        main_menu.add_cascade(label="Добавить элемент", menu=add_menu)
        main_menu.add_command(label="Рассчитать",  command=self.calculate)
        main_menu.add_command(label="Сохранить как",  command=self.get_scrinshot)
        self.config(menu=main_menu)

    def create_theme_table_view(self):
        style = ttk.Style(self)
        aktualTheme = style.theme_use()
        style.theme_create("dummy", parent=aktualTheme)
        style.theme_use("dummy")
        style.map('Treeview', background=[('selected', '#7d7f7d')])

    def isInCreate(self) -> bool:
        return elements.get_count()["OUT"] == 1

    def get_scrinshot(self):
        try:
            screenshot.save_screenshot(screenshot.get_screenshot(elements))
        except NameError as err:
            messagebox.showerror("Ошибка", err)
        except ValueError:
            messagebox.showerror("Ошибка", "Неверное расширение файла")

    def calculate(self):
        if self.isInCreate():
            try:
                TableView(self, calcylate(elements))
            except NameError as err:
                messagebox.showerror("Ошибка", err)
            except RecursionError:
                messagebox.showerror("Ошибка", "Схема зациклена")
        else:
            messagebox.showerror("Ошибка", "Необходимо создать выход")

    def add_out(self):
        if not self.isInCreate():
            elements.add_element(create_element("OUT", self.bacgroung))
        else:
            messagebox.showerror("Ошибка", "Выход может быть только один")
