from UI.Element import Element
from data.Elements import elements


class NO(Element):
    def __init__(self, root, name):
        super(NO, self).__init__(root, name, image_size_x=85, image_size_y=42)
        self.inputs = [["0", "-1"]]
        self.name_inputs = ["0"]
        self.coords_inputs = [18]
        self.coords_outputs = [18]
        self.init_view()

    def get_outputs(self) -> list:
        return ["0"]

    def get_outputs_value(self, params) -> list:
        self.update_inputs_value(params)
        return [not self.inputs_value[0]]