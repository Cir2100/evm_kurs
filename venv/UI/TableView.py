import tkinter as tk
from tkinter import ttk
from screeninfo import get_monitors


class TableView(tk.Toplevel):
    def __init__(self, root, elements):
        super(TableView, self).__init__(root)

        self.width_column = 20
        self.title("Результаты")
        monitor = get_monitors()[0]
        self.geometry(f"{300}x{min(680, monitor.height)}+0+0")
        self.init_view()
        self.insert_data(elements)
        self.grab_set()
        self.focus_set()

    def init_view(self):
        columns = ("K", "L", "X", "Y", "Z", "F")
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        for col in columns:
            self.tree.column(col, width=self.width_column, anchor=tk.CENTER)
            self.tree.heading(col, text=col)

        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        self.tree.tag_configure('even', background='#E8E8E8')
        self.tree.tag_configure('odd', background='#DFDFDF')

        self.tree.pack(fill="both", expand=True)

    def insert_data(self, elements):
        for i in range(len(elements)):
            tags = ('even',)
            if i % 2 == 1:
                tags =  ('odd',)
            self.tree.insert(parent="", index="end", values=elements[i], tags=tags)