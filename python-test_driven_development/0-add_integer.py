#!/usr/bin/python3
"""
Module 0-add_integer
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers a, b

    Arguments:
        a, b
    The values a and b must be int or float

    Return:
        a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
