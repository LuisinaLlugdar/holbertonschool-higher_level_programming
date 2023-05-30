#!/usr/bin/python3
for decenas in range(0, 10):
    for unidades in range(decenas+1, 10):
        if decenas != 8:
            print(f"{decenas}{unidades}", end=', ')
        else:
            print(f"{decenas}{unidades}")
