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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json representation of a list """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Update the class Base by adding the class method
            def save_to_file(cls, list_objs): that writes the JSON
            string representation of list_objs to a file:
        """

        filename = "{}.json".format(__cls.name__)
        with open(filename, 'w', encoding="utf-8") as fid:
            if list_objs is None or list_objs == []:
                json.dump("[]", fid)
            else:
                res = cls.to_json_string(list_objs)
                json.dump(res, fid)
