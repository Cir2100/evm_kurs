import tkinter as tk
from tkinter import messagebox

from UI.MS import create_MS
from UI.CD import create_CD
from UI.DC import create_DC
from UI.NO import create_NO
from UI.OUT import create_OUT
from data.Elements import elements
from data.calcylate import calcylate

class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Рисуем вторую лабу")
        self.geometry("800x600+200+100")
        self.create_menu()
        self.mainloop()

    def create_menu(self):
        add_menu = tk.Menu(master=self)
        add_menu.add_command(label="Мультиплексор", command=self.add_mul)
        add_menu.add_command(label="Дешифратор", command=self.add_dc)
        add_menu.add_command(label="Шифратор", command=self.add_cd)
        add_menu.add_command(label="Не", command=self.add_no)
        add_menu.add_command(label="Выход", command=self.add_out)
        main_menu = tk.Menu(master=self, tearoff=0)
        main_menu.add_cascade(label="Добавить элемент", menu=add_menu)
        main_menu.add_command(label="Рассчитать",  command=self.calculate)
        self.config(menu=main_menu)

    def isInCreate(self) -> bool:
        return elements.get_count()["OUT"] == 1

    def calculate(self):
        if self.isInCreate():
            try:
                calcylate(elements)
            except NameError as err:
                messagebox.showerror("Ошибка", err)
            except RecursionError as err:
                messagebox.showerror("Ошибка", "Схема зациклена")
        else:
            messagebox.showerror("Ошибка", "Необходимо создать выход")

    def add_mul(self):
        create_MS(self)

    def add_dc(self):
        create_DC(self)

    def add_cd(self):
        create_CD(self)

    def add_no(self):
        create_NO(self)

    def add_out(self):
        if not self.isInCreate():
            create_OUT(self)
        else:
            messagebox.showerror("Ошибка", "Выход может быть только один")
