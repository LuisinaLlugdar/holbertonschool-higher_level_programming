#!/usr/bin/python3
"""
Module 2-append_write
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename: the name of the file to append in
        text: the text to append in the file

    Return:
        number of characters appended
    """
    with open(filename, mode='a', encoding='UTF-8') as file:
        return file.write(text)
