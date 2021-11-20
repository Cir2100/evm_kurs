import pyautogui
from tkinter import filedialog

def get_screenshot(elements):
    if (len(elements) == 0):
        raise NameError("Схема пустая")
    max_x = -1
    max_y = -1
    for element in elements:
        max_x = min(max_x, element.winfo_rootx() + element.image_size_x)
        max_y = min(max_y, element.winfo_rooty() + element.image_size_x)
    screenshot = pyautogui.screenshot(region=(element.root.winfo_rootx(),
                                          element.root.winfo_rooty(),
                                          max_x, max_y))
    return screenshot

def save_screenshot(screenshot):
    file = filedialog.asksaveasfile(title="Сохранить схему", defaultextension=".png",
                                    filetypes=[("Png image", "*.png"),
                                               ("JPEG image", "*.jpeg"),
                                               ("JPG image", "*.jpg"),
                                               ("all files", "*.*")])
    if file is not None:
        screenshot.save(file.name)