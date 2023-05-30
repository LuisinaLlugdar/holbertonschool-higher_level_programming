#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        letter = ord(letter)
        if 96 < letter < 123:
            letter -= 32
        print("{}".format(chr(letter)), end="")
    print()
