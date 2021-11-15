def calcylate(elements) -> list:
    ans = []
    for K in range(2):
        for L in range(2):
            for X in range(2):
                for Y in range(2):
                    for Z in range(2):
                        ans.append([K, L, X, Y, Z,
                                    elements[elements.get_index_out()].get_outputs_value([K, L, X, Y, Z])[0]])
    return ans