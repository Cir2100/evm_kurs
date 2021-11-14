import math

from UI.Element import Element
from data.Elements import elements


class DC(Element):
    def __init__(self, root, name):
        super(DC, self).__init__(root, name)
        self.inputs = [["0", "-1"], ["0", "-1"]]
        self.name_inputs = ["0", "1"]
        self.init_view()

    def init_view(self):
       self.inputsTextview.append(self.create_text(self.start_text, 38, text=self.inputs[0][0]))
       self.inputsTextview.append(self.create_text(self.start_text, 80, text=self.inputs[1][0]))

    def get_outputs(self) -> list:
        return ["0", "1", "2", "3"]

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        outputs = [0] * int(math.pow(2, len(self.inputs_value)))
        index_in = 0
        for i in range(len(self.inputs_value)):
            index_in += int(math.pow(2, i)) * self.inputs_value[i]
        outputs[index_in] = 1
        return outputs

def create_DC(root):
    name = "DC" + str(elements.get_count()["DC"] + 1)
    elements.add_element(DC(root, name))