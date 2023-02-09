#!/usr/bin/python3
"""
    This module contains the base class of the project
    test should be in the directory ../tests/test_models/test_base.py
    - private class attribute __nb_objects
    - class constructor
    The goal of it is to manage id attribute in all your future
    classes and to avoid duplicating the same code (by extension, same bugs)
"""


class Base:
    """
        The base class of thhe project.
        Manages id and object instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes the id of the object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
