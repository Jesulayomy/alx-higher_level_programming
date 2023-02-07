#!/usr/bin/python3
"""
    Write a script that adds all arguments to a Python list,
    and then save them to a file:

    You must use your function save_to_json_file
    frm 5-save_to_json_file.py
    You must use your function load_from_json_file
    from 6-load_from_json_file.py
    The list must be saved as a JSON representation
    in a file named add_item.json
"""


import json


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    c_json = load_from_json_file(filename)
except FileNotFoundError:
    c_json = []
except json.decoder.JSONDecodeError:
    c_json = []

for item in sys.argv[1:]:
    c_json += [item]
save_to_json_file(c_json, filename)
