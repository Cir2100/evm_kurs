import pyautogui
from tkinter import filedialog

def get_scrinshot(elements):
    if (len(elements) == 0):
        raise NameError("Схема пустая")
    max_x = -1
    max_y = -1
    for element in elements:
        max_x = max(max_x, element.winfo_rootx() + element.image_size_x)
        max_y = max(max_y, element.winfo_rooty() + element.image_size_x)
    scrinschot = pyautogui.screenshot(region=(element.root.winfo_rootx(),
                                          element.root.winfo_rooty(),
                                          max_x, max_y))
    return scrinschot

def save_scrinschot(scrinschot):
    file = filedialog.asksaveasfile(title="Сохранить схему", defaultextension=".png",
                                    filetypes=[("Png image", "*.png"),
                                               ("JPEG image", "*.jpeg"),
                                               ("JPG image", "*.jpg"),
                                               ("all files", "*.*")])
    if file is not None:
        scrinschot.save(file.name)