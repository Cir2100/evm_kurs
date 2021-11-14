from UI.Element import Element
from data.Elements import elements


class CD(Element):
    def __init__(self, root, name):
        super(CD, self).__init__(root, name)
        self.inputs = [["0", "-1"]]
        self.name_inputs = ["0"]
        self.init_view()

    def init_view(self):
        self.inputsTextview.append(self.create_text(self.start_text, 60, text=self.inputs[0][0]))

    def get_outputs(self) -> list:
        return ["0"]

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        return [not self.inputs_value[0]]

def create_NO(root):
    name = "NO" + str(elements.get_count()["NO"] + 1)
    elements.add_element(CD(root, name))