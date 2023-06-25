#!/usr/bin/python3
"""
Module 1-write_file
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename: the name of the file to write in
        text: the text to write in the file

    Return:
        number of characters written
    """
    with open(filename, mode='w', encoding='UTF-8') as file:
        return file.write(text)
