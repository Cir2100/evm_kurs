from UI.Element import Element
from UI.SettingFrame import SettingFrame


class DC(Element):
    def __init__(self, root):
        super(DC, self).__init__(root, "DC")
        self.inputs = ["0", "0"]
        self.init_view()

    def init_view(self):
       self.inputsID.append(self.create_text(12, 38, text=self.inputs[0]))
       self.inputsID.append(self.create_text(12, 80, text=self.inputs[1]))

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, "DC1", self)
        settingFrame.add_input("0", self.inputs[0])
        settingFrame.add_input("1", self.inputs[1])