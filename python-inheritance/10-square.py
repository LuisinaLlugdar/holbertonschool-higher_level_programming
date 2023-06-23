#!/usr/bin/python3
"""
Module 10-square
based on 9-rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Arguments:
            width
            height
        both private, ints > 0, validated by integer_validator
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        implementation of the area method that cames from BaseGeometry

        Return:
            area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        To modify the print() function, and made it return a specific
        description of the rectangle.


        Return:
            [Rectangle] <width>/<height>
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


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
