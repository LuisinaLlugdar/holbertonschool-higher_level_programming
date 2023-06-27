#!/usr/bin/python3
"""
Module 2-Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherit from Base Class

    Private Attributes:
        width
        height
        x
        y
    Each one of these have their own getter and setter
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for an instance of the class Rectangle

        Args:
            width
            height
            x
            y
            id - comes from the Super Class Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """
            Getter for width
            """
            return self.__width

        @width.setter
        def width(self, width):
            """
            Setter for width
            """
            self.__width = width

        @property
        def height(self):
            """
            Getter for height
            """
            return self.__height

        @height.setter
        def height(self, height):
            """
            Setter for height
            """
            self.__height = height

        @property
        def x(self):
            """
            Getter for x
            """
            return self.__x

        @x.setter
        def x(self, x):
            """
            Setter for x
            """
            self.__x = x

        @property
        def y(self):
            """
            Getter for y
            """
            return self.__y

        @y.setter
        def y(self, y):
            """
            Setter for y
            """
            self.__y = y
