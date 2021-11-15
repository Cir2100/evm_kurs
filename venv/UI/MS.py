import math

from UI.Element import Element
from data.Elements import elements


class MS(Element):
    def __init__(self, root, name):
        super(MS, self).__init__(root, name)
        self.order = 2
        self.coords_inputs = [18, 34, 63, 82, 101, 119]
        self.coords_outputs = [68]
        self.create_inputs()
        self.init_view()

    def create_inputs(self):
        for i in range(self.order):
            self.inputs.append(["0", "1"])
            self.name_inputs.append(f"A{i}")
        for i in range(int(math.pow(2, self.order))):
            self.inputs.append(["0", "1"])
            self.name_inputs.append(f"D{i}")

    def get_outputs(self) -> list:
        return list("F")

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        outputs = [0]
        index_in = 0
        for i in range(self.order):
            index_in += int(math.pow(2, i)) * self.inputs_value[i]
        outputs[0] = self.inputs_value[index_in + self.order];
        return outputs
