from UI.Element import Element
from data.Elements import elements


class OUT(Element):
    def __init__(self, root, name):
        super(OUT, self).__init__(root, name)
        self.inputs = [["0", "-1"]]
        self.name_inputs = ["0"]
        self.coords_inputs = [68]
        #self.coords_outputs = [68]
        self.init_view()

    def get_outputs(self) -> list:
        return ["0"]

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        return self.inputs_value