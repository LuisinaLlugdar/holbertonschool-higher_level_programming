#!/usr/bin/python3
"""
Module 4-from_json_string
"""
import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: the JSON string to be converted into Python object

    Return:
        the object after being transformed
    """
    return json.loads(my_str)
