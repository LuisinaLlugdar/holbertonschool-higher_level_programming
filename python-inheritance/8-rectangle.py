#!/usr/bin/python3
"""
Module 8-rectangle
based on 7-base_geometry
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
