#!/usr/bin/python3
"""
Module 7-add_item
Script that adds all arguments to a Python list,
and then save them to a file named add_item.json
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    obj = []

save_to_json_file(obj + argv[1:], filename)
