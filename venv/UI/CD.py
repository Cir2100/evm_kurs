from UI.Element import Element
from UI.SettingFrame import SettingFrame
from data.Elements import elements


class CD(Element):
    def __init__(self, root, name):
        super(CD, self).__init__(root, name)
        self.inputs = ["1", "0", "0", "0"]
        self.inputs_ids = [[1, -1] ,[0, -1] , [0, -1], [0, -1]]
        self.init_view()

    def init_view(self):
        self.inputsTextview.append(self.create_text(self.start_text, 20, text=self.inputs[0]))
        self.inputsTextview.append(self.create_text(self.start_text, 47, text=self.inputs[1]))
        self.inputsTextview.append(self.create_text(self.start_text, 74, text=self.inputs[2]))
        self.inputsTextview.append(self.create_text(self.start_text, 100, text=self.inputs[3]))

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, self.name, self)
        settingFrame.add_input("0", self.inputs_ids[0])
        settingFrame.add_input("1", self.inputs_ids[1])
        settingFrame.add_input("2", self.inputs_ids[2])
        settingFrame.add_input("3", self.inputs_ids[3])

    def get_outputs(self) -> list:
        return ["0", "1"]

def create_CD(root):
    name = "CD" + str(elements.get_count()["CD"] + 1)
    elements.add_element(CD(root, name))