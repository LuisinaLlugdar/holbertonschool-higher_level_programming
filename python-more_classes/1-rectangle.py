#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle with private attributes width and height

    Attributes:
        height: the height of the rectangle, private
        width: the width of the rectangle, private
    both attributes must be integers >= 0
    """
    def __init__(self, width=0, height=0):
        """
        initializes an instance of class Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
