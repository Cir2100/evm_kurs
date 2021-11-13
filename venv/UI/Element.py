import tkinter as tk
from tkinter import ttk
from abc import ABCMeta, abstractmethod

inputs_dict = {0: "0", 1: "1", 2: "K", 3: "L", 4: "X", 5: "Y", 6: "Z"}

class Element(tk.Canvas, metaclass=ABCMeta):
    def __init__(self, root, name):
        self.image_size_x = 140
        self.image_size_y = 134
        super(Element, self).__init__(root, width=self.image_size_x, height=self.image_size_y, bg='white')
        self.pack()
        self.place(x=0, y=0, anchor=tk.NW)
        self.bind("<B1-Motion>", self.move)
        self.bind("<Double-Button-1>", lambda event: self.create_setting_dialog())
        self.bind("<Button-3>", self.create_dialog_menu)

        self.img = tk.PhotoImage(file=f"venv\\resources\\{name}.png")
        imagesprite = self.create_image(0, 0, image=self.img, anchor=tk.NW)

        self.root = root
        self.inputs = []
        self.inputsID = []

    def move(self, event):
        coord_x = min(max(event.x_root - self.root.winfo_rootx(), self.image_size_x / 2),
                      self.root.winfo_width() - self.image_size_x / 2)
        coord_y = min(max(event.y_root - self.root.winfo_rooty(), self.image_size_y / 2),
                      self.root.winfo_height() - self.image_size_y / 2)
        self.place(x=coord_x, y=coord_y, anchor=tk.CENTER)

    def create_dialog_menu(self, event):
        menu = tk.Menu(master=self.root, tearoff=0)
        menu.add_command(label="Удалить", command=self.destroy)
        menu.post(event.x_root, event.y_root)

    @abstractmethod
    def create_setting_dialog(self):
        raise NotImplementedError("check_ripeness method not implemented!")

    @abstractmethod
    def init_view(self):
        raise NotImplementedError("check_ripeness method not implemented!")

    def update_view(self):
        for i in range(len(self.inputsID)):
            text = inputs_dict[self.inputs[i]] if self.inputs[i] in inputs_dict  else self.inputs[i] # check this
            self.itemconfigure(self.inputsID[i], text=inputs_dict[self.inputs[i]])

    def updateInputs(self, settings):
        self.inputs = settings
        self.update_view()