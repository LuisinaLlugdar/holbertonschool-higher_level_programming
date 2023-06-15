#!/usr/bin/python3
"""
Module 4-print_square
Method that prints a square with #
"""


def print_square(size):
    """
    Function that prints a square with the character #

    Argument:
        size: size of the square to be printed
    size must be a positive integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
