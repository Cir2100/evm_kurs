import tkinter as tk
from tkinter import ttk
from abc import ABCMeta, abstractmethod

from UI.SettingFrame import SettingFrame
from data.Elements import elements
from data.inputs_dict import inputs_dict


class Element(tk.Canvas, metaclass=ABCMeta):
    def __init__(self, root, name):
        self.image_size_x = 160
        self.image_size_y = 145
        self.start_text = 20
        super(Element, self).__init__(root, width=self.image_size_x, height=self.image_size_y, bg='white')
        self.pack()
        self.place(x=0, y=0, anchor=tk.NW)
        self.bind("<B1-Motion>", self.move)
        self.bind("<Double-Button-1>", lambda event: self.create_setting_dialog())
        self.bind("<Button-3>", self.create_dialog_menu)
        self.img = tk.PhotoImage(file=f"venv\\resources\\{name[0:2]}.png")
        imagesprite = self.create_image(20, 0, image=self.img, anchor=tk.NW)

        self.create_text(95, 134, text=name, anchor=tk.N)

        self.root = root
        self.inputs = []
        self.inputsTextview = []
        self.name_inputs = []
        self.inputs_value = []

        self.name = name

    def get_name(self)-> str:
        return self.name

    def move(self, event):
        coord_x = min(max(event.x_root - self.root.winfo_rootx(), self.image_size_x / 2),
                      self.root.winfo_width() - self.image_size_x / 2)
        coord_y = min(max(event.y_root - self.root.winfo_rooty(), self.image_size_y / 2),
                      self.root.winfo_height() - self.image_size_y / 2)
        self.place(x=coord_x, y=coord_y, anchor=tk.CENTER)

    def create_dialog_menu(self, event):
        menu = tk.Menu(master=self.root, tearoff=0)
        menu.add_command(label="Удалить", command=self.delete_elemet)
        menu.post(event.x_root, event.y_root)

    def delete_elemet(self):
        elements.delete_element(self)
        elements.update_inputs()
        self.destroy()

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, self.name, self)
        for i in range(len(self.name_inputs)):
            settingFrame.add_input(self.name_inputs[i], self.inputs[i])

    @abstractmethod
    def init_view(self):
        raise NotImplementedError("check_ripeness method not implemented!")

    @abstractmethod
    def get_outputs(self) -> list:
        raise NotImplementedError("check_ripeness method not implemented!")

    def get_inputs(self) -> list:
        return self.inputs

    def update_inputs(self):
        self.update_view()

    def update_inputs_value(self, params):
        self.inputs_value.clear()
        for cur_input in self.inputs:
            if cur_input[1] != "-1":
                index_element = elements.index(cur_input[0])
                self.inputs_value.append(elements[index_element].
                                         get_outputs_value(params)[elements[index_element].
                                         get_outputs().index(cur_input[1])])
            else:
                index_element = inputs_dict[cur_input[0]]
                if index_element < 2:
                    self.inputs_value.append(index_element)
                else:
                    self.inputs_value.append(params[index_element - 2])

    @abstractmethod
    def get_outputs_value(self, params) -> list:
        raise NotImplementedError("check_ripeness method not implemented!")

    def update_view(self):
        for i in range(len(self.inputsTextview)):
            text = self.inputs[i][0]
            if self.inputs[i][1] != "-1":
                text += "." + self.inputs[i][1]
                if self.inputs[i][0] not in elements.get_names():
                    text = "0"
                    self.inputs[i] = ["0", "-1"]
            self.itemconfigure(self.inputsTextview[i], text=text)


    def updateInputs(self, settings):
        self.inputs = settings
        self.update_inputs()