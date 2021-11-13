from tkinter import ttk
import tkinter as tk


class SettingFrame(tk.Toplevel):
    def __init__(self, root, name, parent):
        super(SettingFrame, self).__init__(root)
        self.title(name)
        self.geometry("200x180+400+300")
        self.resizable(False, False)
        self.init_view()
        self.grab_set()
        self.focus_set()
        self.attr_y = 10
        self.combodxs = []
        self.parent = parent

    def init_view(self):
        self.button_ok = ttk.Button(self, text='ОК', command=self.set_settings)
        self.button_ok.place(x=5, y=150)

        button_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        button_cancel.place(x=120, y=150)

    def add_input(self, name, current):
        label_selection = tk.Label(self, text=f"Вход {name}")
        label_selection.place(x=10, y=self.attr_y)

        self.combobx = ttk.Combobox(self, values=[u"0", u"1", u"K", u"L", u"X", u"Y", u"Z"], width=1)
        self.combobx.current(current)
        self.combobx.place(x=60, y=self.attr_y)
        self.combodxs.append(self.combobx)

        self.attr_y += 20

    def set_settings(self):
        settings = []
        for combodx in self.combodxs:
            settings.append(combodx.current())
        self.parent.updateInputs(settings)
        self.destroy()