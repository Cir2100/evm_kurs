import tkinter as tk
from UI.MS import MS
from UI.CD import CD
from UI.DC import DC

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
        self.config(menu=main_menu)

    def add_mul(self):
        MS(self)

    def add_dc(self):
        DC(self)

    def add_cd(self):
        CD(self)

    def add_no(self):
        NO(self)