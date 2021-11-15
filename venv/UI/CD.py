import math

from UI.Element import Element
from data.Elements import elements


class CD(Element):
    def __init__(self, root, name):
        super(CD, self).__init__(root, name)
        self.inputs = [["1", "-1"], ["0", "-1"], ["0", "-1"], ["0", "-1"]]
        self.name_inputs = ["0", "1", "2", "3"]
        self.coords_inputs = [28, 55, 81, 107]
        self.coords_outputs = [45, 89]
        self.init_view()

    def get_outputs(self) -> list:
        return ["0", "1"]

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        is_one = False
        for inp in self.inputs_value:
            if inp == 1:
                is_one = True
        if not is_one:
            raise NameError("На шифраторе должна быть хотябы одна единица")
        outputs = [0] * len(self.get_outputs())
        index_in = 0
        for i in range(len(self.inputs_value) - 1, -1, -1):
            if self.inputs_value[i] == 1:
                index_in = i
                break
        i = 0
        while index_in > 0:
            if index_in % 2 != 0:
                outputs[i] = 1
            index_in = index_in // 2
            i += 1
        return outputs