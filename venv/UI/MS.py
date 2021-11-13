from UI.Element import Element
from UI.SettingFrame import SettingFrame


class MS(Element):
    def __init__(self, root):
        super(MS, self).__init__(root, "MS")
        self.inputs = ["0", "0", "0", "0", "0", "0"]
        self.root = root
        self.init_view()

    def init_view(self):
        self.inputsID.append(self.create_text(12, 10, text=self.inputs[0]))
        self.inputsID.append(self.create_text(12, 27, text=self.inputs[1]))
        self.inputsID.append(self.create_text(12, 55, text=self.inputs[2]))
        self.inputsID.append(self.create_text(12, 75, text=self.inputs[3]))
        self.inputsID.append(self.create_text(12, 94, text=self.inputs[4]))
        self.inputsID.append(self.create_text(12, 112, text=self.inputs[5]))

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, "MS1", self)
        settingFrame.add_input("A0", self.inputs[0])
        settingFrame.add_input("A1", self.inputs[1])
        settingFrame.add_input("D0", self.inputs[2])
        settingFrame.add_input("D1", self.inputs[3])
        settingFrame.add_input("D2", self.inputs[4])
        settingFrame.add_input("D3", self.inputs[5])