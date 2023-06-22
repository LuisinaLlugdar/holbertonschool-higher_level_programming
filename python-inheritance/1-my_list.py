#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """
    class that inherits from list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        ordered_list = sorted(self)
        print(ordered_list)
