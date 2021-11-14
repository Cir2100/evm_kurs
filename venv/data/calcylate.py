def calcylate(elements):
    print("start")
    for K in range(2):
        for L in range(2):
            for X in range(2):
                for Y in range(2):
                    for Z in range(2):
                        print([K, L, X, Y, Z], end=' ')
                        print(elements[elements.get_index_out()].get_outputs_value([K, L, X, Y, Z])[0])