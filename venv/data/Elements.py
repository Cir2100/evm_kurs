class Elements():
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def get_count(self) -> dict:
        count = {"MS": 0, "CD": 0, "DC": 0, "NO": 0, "OUT" : 0}
        for element in self.elements:
            for key in count.keys():
                if key in element.get_name():
                    count[key] += 1
        return count

    def get_names_without_this(self, name) -> list:
        names = []
        for element in self.elements:
            if element.get_name() != name and element.get_name() != "OUT":
                names.append(element.get_name())
        return names

    def get_names(self) -> list:
        names = []
        for element in self.elements:
            names.append(element.get_name())
        return names

    def delete_element(self, obj):
        self.elements.remove(obj)

    def update_view(self):
        for element in self.elements:
            element.update_view()

    def print_info(self):
        print("Info:")
        for element in self.elements:
            print(element.get_name())
        print()

    def index(self, name) -> int:
        for i in range(len(self.elements)):
            if name == self.elements[i].get_name():
                return i
        return -1

    def get_index_out(self):
        for i in range(len(self.elements)):
            if "OUT" == self.elements[i].get_name():
                return i
        return -1

    def __getitem__(self, i):
        return self.elements[i]

    def __len__(self):
        return len(self.elements)

elements = Elements()
