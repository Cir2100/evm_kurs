from UI.Element import Element
from UI.SettingFrame import SettingFrame
from data.Elements import elements


class DC(Element):
    def __init__(self, root, name):
        super(DC, self).__init__(root, name)
        self.inputs = ["0", "0"]
        self.inputs_ids = [[0, -1], [0, -1]]
        self.init_view()

    def init_view(self):
       self.inputsTextview.append(self.create_text(self.start_text, 38, text=self.inputs[0]))
       self.inputsTextview.append(self.create_text(self.start_text, 80, text=self.inputs[1]))

    def create_setting_dialog(self):
        settingFrame = SettingFrame(self.root, self.name, self)
        settingFrame.add_input("0", self.inputs_ids[0])
        settingFrame.add_input("1", self.inputs_ids[1])

    def get_outputs(self) -> list:
        return ["0", "1", "2", "3"]

def create_DC(root):
    name = "DC" + str(elements.get_count()["DC"] + 1)
    elements.add_element(DC(root, name))