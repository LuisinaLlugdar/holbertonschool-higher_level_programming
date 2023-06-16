#!/usr/bin/python3
"""
Module 5-text_indentation
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text: text to be printed, applying the changes
              said before
    The text has to be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    char_before = 0
    for i in range(len(text)):
        if char_before is 1:
            char_before = 0
            if text[i] == " ":
                continue
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            char_before = 1
