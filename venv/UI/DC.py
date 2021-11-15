import math

from UI.Element import Element
from data.Elements import elements


class DC(Element):
    def __init__(self, root, name):
        super(DC, self).__init__(root, name)
        self.inputs = [["0", "-1"], ["0", "-1"]]
        self.name_inputs = ["0", "1"]
        self.coords_inputs = [46, 89]
        self.coords_outputs = [28, 55, 81, 107]
        self.init_view()

    def get_outputs(self) -> list:
        return ["0", "1", "2", "3"]

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        #outputs = [0] * int(math.pow(2, len(self.inputs_value)))
        outputs = [0] * len(self.get_outputs())
        index_in = 0
        for i in range(len(self.inputs_value)):
            index_in += int(math.pow(2, i)) * self.inputs_value[i]
        outputs[index_in] = 1
        return outputs