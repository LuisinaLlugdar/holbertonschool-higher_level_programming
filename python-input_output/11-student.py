#!/usr/bin/python3
"""
Module 11-student
"""


class Student:
    """
    class Student that defines a student by:
        -Public instance attributes:
            first_name
            last_name
            age
       -Public Methods:
            to_json: retrieves its dictionary representation
            reload_from_json: replaces all attributes of the Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes an instance of Student Class with all
        the public attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of the Student instance

        Args:
            attrs
        """
        if attrs is None:
            return self.__dict__
        else:
            dicti = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dicti[attr] = self.__dict__[attr]
            return dicti

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance

        Args:
            json: will always be a dictionary
        """
        self.first_name = json.get("first_name")
        self.last_name = json.get("last_name")
        self.age = json.get("age")
