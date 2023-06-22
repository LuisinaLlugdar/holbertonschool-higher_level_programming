#!/usr/bin/python3
"""
Module 7-base_geometry
based on 6-base_geometry
"""


class BaseGeometry:
    """
    Public methods:
        area
        integer_validator
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that checks if value is an int > 0

        Arguments:
            name (always str)
            value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
