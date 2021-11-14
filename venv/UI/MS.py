from UI.Element import Element
from UI.SettingFrame import SettingFrame
from data.Elements import elements


class MS(Element):
    def __init__(self, root, name):
        super(MS, self).__init__(root, name)
        self.inputs = ["0", "0", "0", "0", "0", "0"]
        self.inputs_ids = [[0, -1], [0, -1], [0, -1], [0, -1], [0, -1], [0, -1]]
        self.init_view()

    def init_view(self):
        self.inputsTextview.append(self.create_text(self.start_text, 10, text=self.inputs[0]))
        self.inputsTextview.append(self.create_text(self.start_text, 27, text=self.inputs[1]))
        self.inputsTextview.append(self.create_text(self.start_text, 55, text=self.inputs[2]))
        self.inputsTextview.append(self.create_text(self.start_text, 75, text=self.inputs[3]))
        self.inputsTextview.append(self.create_text(self.start_text, 94, text=self.inputs[4]))
        self.inputsTextview.append(self.create_text(self.start_text, 112, text=self.inputs[5]))

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, self.name, self)
        settingFrame.add_input("A0", self.inputs_ids[0])
        settingFrame.add_input("A1", self.inputs_ids[1])
        settingFrame.add_input("D0", self.inputs_ids[2])
        settingFrame.add_input("D1", self.inputs_ids[3])
        settingFrame.add_input("D2", self.inputs_ids[4])
        settingFrame.add_input("D3", self.inputs_ids[5])

    def get_outputs(self) -> list:
        return list("F")


def create_MS(root):
    name = "MS" + str(elements.get_count()["MS"] + 1)
    elements.add_element(MS(root, name))
