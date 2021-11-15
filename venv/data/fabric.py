from UI.Element import Element
from UI.MS import MS
from UI.CD import CD
from UI.DC import DC
from UI.NO import NO
from UI.OUT import OUT
from data.Elements import elements

def create_element(name, root) -> Element:
    name = name + str(elements.get_count()[name] + 1)
    if (name[0:2] == "MS"):
        return MS(root, name)
    elif (name[0:2] == "DC"):
        return DC(root, name)
    elif (name[0:2] == "CD"):
        return CD(root, name)
    elif (name[0:2] == "NO"):
        return NO(root, name)
    elif (name[0:3] == "OUT"):
        return OUT(root, "OUT")