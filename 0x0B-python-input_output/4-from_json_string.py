#!/usr/bin/python3
"""
    Returns a PyObject frm a string
"""


import json


def from_json_string(my_str):
    """
        string to object converter
    """

    obj = json.load(my_str)
    return obj
