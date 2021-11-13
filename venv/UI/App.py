import tkinter as tk
from UI.MS import create_MS
from UI.CD import create_CD
from UI.DC import create_DC
from data.Elements import elements

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
        main_menu = tk.Menu(master=self, tearoff=0)
        main_menu.add_cascade(label="Добавить элемент", menu=add_menu)
        main_menu.add_command(label="Проверить",  command=self.check)
        self.config(menu=main_menu)

    def check(self):
        elements.print_info()

    def add_mul(self):
        create_MS(self)

    def add_dc(self):
        create_DC(self)

    def add_cd(self):
        create_CD(self)

    def add_no(self):
        create_NO(self)