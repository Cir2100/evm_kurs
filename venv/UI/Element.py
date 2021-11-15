import tkinter as tk
from tkinter import ttk
from abc import ABCMeta, abstractmethod

from UI.SettingFrame import SettingFrame
from data.Elements import elements
from data.inputs_dict import inputs_dict


class Element(tk.Canvas, metaclass=ABCMeta):
    def __init__(self, root, name, image_size_x = 165, image_size_y = 145):
        self.image_size_x = image_size_x
        self.image_size_y = image_size_y
        self.start_text = 20

        super(Element, self).__init__(root, width=self.image_size_x, height=self.image_size_y, bg='white', bd=0)

        self.root = root
        self.inputs = []
        self.inputsTextview = []
        self.name_inputs = []
        self.inputs_value = []
        self.coords_inputs=[]
        self.coords_outputs=[]
        self.name = name

        self.lines = []

    def init_view(self):
        self.pack()
        self.place(x=0, y=0, anchor=tk.NW)
        self.bind("<B1-Motion>", self.move)
        self.bind("<Double-Button-1>", lambda event: self.create_setting_dialog())
        self.bind("<Button-3>", self.create_dialog_menu)
        self.img = tk.PhotoImage(file=f"venv\\resources\\{self.name[0:2]}.png")
        imagesprite = self.create_image(20, 0, image=self.img, anchor=tk.NW)

        self.create_text(95, 134, text=self.name, anchor=tk.N)

        for i in range(len(self.coords_inputs)):
            self.inputsTextview.append(self.create_text(self.start_text, self.coords_inputs[i] - 8, text=self.inputs[i][0]))
            self.create_line(0, self.coords_inputs[i], 25, self.coords_inputs[i])

        for coordinate in self.coords_outputs:
            self.create_line(self.image_size_x - 15, coordinate, self.image_size_x + 10, coordinate)


    def get_name(self)-> str:
        return self.name

    def move(self, event):
        coord_x = min(max(event.x_root - self.root.winfo_rootx(), self.image_size_x / 2),
                      self.root.winfo_width() - self.image_size_x / 2)
        coord_y = min(max(event.y_root - self.root.winfo_rooty(), self.image_size_y / 2),
                      self.root.winfo_height() - self.image_size_y / 2)
        self.place(x=coord_x, y=coord_y, anchor=tk.CENTER)
        self.update_view()

    def create_dialog_menu(self, event):
        menu = tk.Menu(master=self.root, tearoff=0)
        menu.add_command(label="Удалить", command=self.delete_elemet)
        menu.post(event.x_root, event.y_root)

    def delete_elemet(self):
        elements.delete_element(self)
        elements.update_view()
        self.destroy()

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, self.name, self)
        for i in range(len(self.name_inputs)):
            settingFrame.add_input(self.name_inputs[i], self.inputs[i])

    @abstractmethod
    def get_outputs(self) -> list:
        raise NotImplementedError("check_ripeness method not implemented!")

    def get_inputs(self) -> list:
        return self.inputs

    def get_coordinate_outputs(self) -> list:
        return self.coords_outputs

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

    def delete_lines(self):
        for line in self.lines:
            self.root.delete(line)
        self.lines.clear()

    def add_line(self, index):
        index_from = elements.index(self.inputs[index][0])
        index_output_from = elements[index_from].get_outputs().index(self.inputs[index][1])
        self.lines.append(self.root.add_line(elements[index_from].winfo_rootx() - self.root.winfo_rootx() + 140,
                           elements[index_from].winfo_rooty() - self.root.winfo_rooty() +
                           elements[index_from].get_coordinate_outputs()[index_output_from],
                           self.winfo_rootx() - self.root.winfo_rootx() + self.start_text,
                           self.winfo_rooty() - self.root.winfo_rooty() + self.coords_inputs[index]))

    @abstractmethod
    def get_outputs_value(self, params) -> list:
        raise NotImplementedError("check_ripeness method not implemented!")

    def update_view(self):
        self.delete_lines()
        for i in range(len(self.inputsTextview)):
            text = self.inputs[i][0]
            if self.inputs[i][1] != "-1":
                if self.inputs[i][0] in elements.get_names():
                    text = ""
                    self.add_line(i)
                else:
                    text = "0"
                    self.inputs[i] = ["0", "-1"]
            self.itemconfigure(self.inputsTextview[i], text=text)


    def updateInputs(self, settings):
        self.inputs = settings
        self.update_view()