import math

from UI.Element import Element
from data.Elements import elements


class CD(Element):
    def __init__(self, root, name):
        super(CD, self).__init__(root, name)
        self.inputs = [["1", "-1"] ,["0", "-1"] , ["0", "-1"], ["0", "-1"]]
        self.name_inputs = ["0", "1", "2", "3"]
        self.init_view()

    def init_view(self):
        self.inputsTextview.append(self.create_text(self.start_text, 20, text=self.inputs[0][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 47, text=self.inputs[1][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 74, text=self.inputs[2][0]))
        self.inputsTextview.append(self.create_text(self.start_text, 100, text=self.inputs[3][0]))

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
        outputs = [0] * int(math.log2(len(self.inputs_value)))
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

def create_CD(root):
    name = "CD" + str(elements.get_count()["CD"] + 1)
    elements.add_element(CD(root, name))