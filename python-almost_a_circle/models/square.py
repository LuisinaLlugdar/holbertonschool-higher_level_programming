#!/usr/bin/python3
"""
Module 3-Square
"""

from models.rectangle import Rectangle
"""
Importing Rectangle Class to be inherited
"""


class Square(Rectangle):
    """
    Class Square that inherit from Rectangle Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for an instance of the class Square

        Args:
            size (for both width and height)
            x
            y
            id
        they must me inherited from Rectangle
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriding the __str__ method so that it returns a specific message
        """
        msg = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.width)
        return msg

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for size

        Args:
            size: the size of the square
        """
        self.width = size
        self.height = size
