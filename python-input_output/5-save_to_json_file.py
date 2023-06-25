#!/usr/bin/python3
"""
Module 5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj: python object to be transformed into JSON
        filename: name of the file to write the JSON object into
    """
    with open(filename, mode='w', encoding='UTF-8') as file:
        transformed_obj = json.dumps(my_obj)
        return file.write(transformed_obj)
