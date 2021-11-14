import math

from UI.Element import Element
from data.Elements import elements


class MS(Element):
    def __init__(self, root, name):
        super(MS, self).__init__(root, name)
        self.inputs = [["0", "-1"], ["0", "-1"], ["0", "-1"], ["0", "-1"], ["0", "-1"], ["0", "-1"]]
        self.name_inputs = ["A0", "A1", "D0", "D1", "D2", "D3"]
        self.init_view()

    def init_view(self):
        self.inputsTextview.append(self.create_text(self.start_text, 10, text=self.inputs[0][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 27, text=self.inputs[1][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 55, text=self.inputs[2][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 75, text=self.inputs[3][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 94, text=self.inputs[4][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 112, text=self.inputs[5][0]))

    def get_outputs(self) -> list:
        return list("F")

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        outputs = [0]
        index_in = 0
        for i in range(2):
            index_in += int(math.pow(2, i)) * self.inputs_value[i]
        outputs[0] = self.inputs_value[index_in + 2];
        return outputs


def create_MS(root):
    name = "MS" + str(elements.get_count()["MS"] + 1)
    elements.add_element(MS(root, name))
