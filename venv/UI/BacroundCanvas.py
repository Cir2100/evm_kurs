import tkinter as tk

class BacgroundCanvas(tk.Canvas):
    def __init__(self, root):
        super(BacgroundCanvas, self).__init__(root, bg='white', highlightthickness=0)
        self.pack(fill="both", expand=True)

    def add_line(self, x1, y1, x2, y2) -> int:
        x_mid = (x1 + x2) // 2
        return self.create_line(x1, y1, x_mid, y1, x_mid, y2, x2, y2)