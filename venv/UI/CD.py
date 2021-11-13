from UI.Element import Element
from UI.SettingFrame import SettingFrame


class CD(Element):
    def __init__(self, root):
        super(CD, self).__init__(root, "CD")
        self.inputs = ["1", "0", "0", "0"]
        self.root = root
        self.init_view()

    def init_view(self):
        self.inputsID.append(self.create_text(12, 20, text=self.inputs[0]))
        self.inputsID.append(self.create_text(12, 47, text=self.inputs[1]))
        self.inputsID.append(self.create_text(12, 74, text=self.inputs[2]))
        self.inputsID.append(self.create_text(12, 100, text=self.inputs[3]))

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, "CD1", self)
        settingFrame.add_input("0", self.inputs[0])
        settingFrame.add_input("1", self.inputs[1])
        settingFrame.add_input("2", self.inputs[2])
        settingFrame.add_input("3", self.inputs[3])