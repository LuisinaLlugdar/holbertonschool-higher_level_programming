#!/usr/bin/python3
"""
Module 1-Base_Class
"""


class Base:
    """
    Class that will be the “base” of all other classes in this project

    Attributes:
        __nb_objects: initialized in 0. Increments each time a new obj created

    Methods:
        __init__: constructor.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor. Assigns id when creates an object, default=None


        Args:
            id: int. Public attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
