#!/usr/bin/python3
for decenas in range(0, 9):
    for unidades in range(decenas+1, 10):
        if decenas != 8:
            print("{}{}".format(decenas, unidades), end=', ')
        else:
            print("{}{}".format(decenas, unidades))
