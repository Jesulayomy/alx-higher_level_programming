#!/usr/bin/python3
"""
    Write a function that reads an Object frm a text file,
    using a JSON representation:
"""


import json


def load_from_json_file(filename):
    """
        reads an object frm textfile
    """

    with open(filename, 'r', encoding="utf-8") as fid:
        obj = json.load(fid)
    return obj
