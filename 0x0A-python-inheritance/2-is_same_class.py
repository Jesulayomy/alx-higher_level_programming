#!/usr/bin/python3
"""
    This module contains a function that checks if an object is an
    instace of a specified class
"""


def is_same_class(obj, a_class):
    """
        Checks if an object is an instance of
        the listed class
    """

    return (type(obj) == a_class)
