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

        Args:
            width: the width of the rectangle, 0 if not specified
            height: the height of the rectangle, 0 if not specified
        both args must be integers >= 0
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

    def area(self):
        """
        Calculates the area of the rectangle

        Return:
            area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Return:
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Prints rectangle with #

        Return:
            the rectangle printed if width and height > 0,
            or an empty string otherwise
        """

        result = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result

    def __repr__(self):
        """
        Recreate new instance with string
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
