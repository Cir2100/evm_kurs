import math

from UI.Element import Element
from data.Elements import elements


class MS(Element):
    def __init__(self, root, name):
        super(MS, self).__init__(root, name)
        self.inputs = [["0", "-1"], ["0", "-1"], ["0", "-1"], ["0", "-1"], ["0", "-1"], ["0", "-1"]]
        self.name_inputs = ["A0", "A1", "D0", "D1", "D2", "D3"]
        self.coords_inputs = [18, 34, 63, 82, 101, 119]
        self.coords_outputs = [68]
        self.init_view()

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
