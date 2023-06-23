#!/usr/bin/python3
"""
Module 10-square
based on 9-rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes size of an object from Square Class

        Arguments:
            size
        size must be a private int >0, validated by integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """
        Method that returns the area of the square
        """
        return self.__size ** 2
