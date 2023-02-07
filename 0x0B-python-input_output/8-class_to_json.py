#!/usr/bin/python3
"""
    Write a function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
"""


def class_to_json(obj):
    """
        returns an object dictionary containing
        the class attributes
    """

    return (obj.__dict__)
