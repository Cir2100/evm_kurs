from tkinter import ttk
import tkinter as tk

from data.Elements import elements
from data.inputs_dict import inputs_dict

class SettingFrame(tk.Toplevel):
    def __init__(self, root, title_str, parent, input_title, inputs_text):
        super(SettingFrame, self).__init__(root)
        self.title(title_str)
        self.geometry("200x190+400+300")
        self.resizable(False, False)
        self.init_view()
        self.grab_set()
        self.focus_set()
        self.attr_y = 10
        self.combodxs = []
        self.additional_combodxs = []
        self.parent = parent
        self.title_str = title_str

        for i in range(len(input_title)):
            self.add_input(input_title[i], inputs_text[i])

    def init_view(self):
        button_ok = ttk.Button(self, text='ОК', command=self.set_settings)
        button_ok.place(x=5, y=160)

        button_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        button_cancel.place(x=120, y=160)

    def add_input(self, name, current):
        label_selection = tk.Label(self, text=f"Вход {name}")
        label_selection.place(x=10, y=self.attr_y)

        values = list(inputs_dict.keys())
        values.extend(elements.get_names_without_this(self.title_str))

        combobx = ttk.Combobox(self, values=values, width=5, state="readonly")
        combobx.current(values.index(current[0]))
        combobx.place(x=60, y=self.attr_y)
        combobx.bind("<<ComboboxSelected>>", self.chouse_element)
        self.combodxs.append(combobx)

        if values.index(current[0]) > 6:
            values = elements[elements.index(combobx.get())].get_outputs()

            additional_combodxs = ttk.Combobox(self, values=values, width=5, state="readonly")
            additional_combodxs.current(values.index(current[1]))
            additional_combodxs.place(x=130, y=self.attr_y)
            additional_combodxs.bind("<<ComboboxSelected>>", self.chouse_element)
            self.additional_combodxs.append(additional_combodxs)

        self.attr_y += 25

    def set_settings(self):
        settings = []
        for combodx in self.combodxs:
            if combodx.current() < 7: #check
                settings.append([combodx.get(), "-1"])
            else:
                for com in self.additional_combodxs:
                    if combodx.winfo_rooty() == com.winfo_rooty():
                        settings.append([combodx.get(), com.get()])
                        break
        self.parent.updateInputs(settings)
        self.destroy()

    def add_additional_combodxs(self, widget):
        name = widget.get()
        combobx = ttk.Combobox(self, values=elements[elements.index(widget.get())].get_outputs(),
                               width=5, state="readonly")
        combobx.current(0)
        combobx.place(x=130, y=widget.winfo_rooty() - self.winfo_rooty())
        self.additional_combodxs.append(combobx)

    def delete_additional_combodxs(self, widget):
        if widget in self.combodxs:
            for com in self.additional_combodxs:
                if widget.winfo_rooty() == com.winfo_rooty():
                    self.additional_combodxs.remove(com)
                    com.destroy()
                    break

    def chouse_element(self, event):
        index = event.widget.current()
        self.delete_additional_combodxs(event.widget)
        if (index > 6):
            self.add_additional_combodxs(event.widget)