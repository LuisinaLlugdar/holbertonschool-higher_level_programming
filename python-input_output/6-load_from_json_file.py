#!/usr/bin/python3
"""
Module 6-load_to_json_file
"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”

    Args:
        filename: JSON file to create an object from
    """
    with open(filename, mode='r', encoding='UTF-8') as file:
        json_obj = file.read()
        python_obj = json.loads(json_obj)
        return python_obj
