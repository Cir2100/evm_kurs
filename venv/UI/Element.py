import tkinter as tk
from tkinter import ttk
from abc import ABCMeta, abstractmethod
from data.Elements import elements
from data.inputs_dict import inputs_dict


class Element(tk.Canvas, metaclass=ABCMeta):
    def __init__(self, root, name):
        self.image_size_x = 155
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

        self.create_text(75, 134, text=name, anchor=tk.N)

        self.root = root
        self.inputs = []
        self.inputsTextview = []
        self.inputs_ids = []

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
        self.destroy()

    @abstractmethod
    def create_setting_dialog(self):
        raise NotImplementedError("check_ripeness method not implemented!")

    @abstractmethod
    def init_view(self):
        raise NotImplementedError("check_ripeness method not implemented!")

    @abstractmethod
    def get_outputs(self) -> list:
        raise NotImplementedError("check_ripeness method not implemented!")

    def update_view(self):
        for i in range(len(self.inputsTextview)):
            self.itemconfigure(self.inputsTextview[i], text=self.inputs[i])
            if self.inputs[i][0] in inputs_dict:
                self.inputs_ids[i] = [inputs_dict[self.inputs[i][0]], -1]
            names = elements.get_names()
            if self.inputs[i][0] in names:
                index = names.index(self.inputs[i][0])
                index_self = names.index(self.name)
                flag = 0
                if index_self < index:
                    flag = 1
                self.inputs_ids[i] =  [index + 7 - flag, elements[index].get_outputs().index(self.inputs[i][1])]


    def updateInputs(self, settings):
        self.inputs = settings
        self.update_view()