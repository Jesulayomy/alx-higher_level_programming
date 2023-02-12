#!/usr/bin/python3
"""
    This module contains the base class of the project
    test should be in the directory ../tests/test_models/test_base.py
    - private class attribute __nb_objects
    - class constructor
    The goal of it is to manage id attribute in all your future
    classes and to avoid duplicating the same code (by extension, same bugs)
"""


import csv
import json
import os.path


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

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as fid:
            if list_objs is None or list_objs == []:
                json.dump("[]", fid)
            else:
                res = cls.to_json_string(list_objs)
                json.dump(res, fid)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with its attributes set """

        new = cls(1, 1)
        new.update(dictionary)

    @classmethod
    def load_from_file(cls):
        """ loads a list of instances froom a file """

        filename = "{}.json".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', encoding="utf-8") as fid:
            list_as_string = f.read()

        list_in_class = cls.from_json_string(list_as_string)
        list_instances = []

        for idx in range(len(list_in_class)):
            list_instances.append(cls.create(**list_in_class[idx]))

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves serialized csv format """

        filename = "{}.csv".format(cls.__name__)
        if filename == "Rectangle.csv":
            list_dict = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dict = [0, 0, 0, 0]
            list_keys = ['id', 'size', 'x', 'y']

        list_of_lists = []
        if not list_objs:
            pass
        else:
            for objt in list_objs:
                for idx in range(len(list_keys)):
                    list_dict[idx] = objt.to_dictionary()[list_keys[idx]]
                list_of_lists.append(list_dict[:])

        with open(filename, 'w') as fid:
            to_file = csv.writer(fid)
            to_file.writerows(list_of_lists)

    @classmethod
    def load_from_file_csv(cls):
        """ loads deserialized csv """

        filename = "{}.csv".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r', encoding="utf-8") as fid:
            values = csv.reader(fid)
            csv_list = list(values)
        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        list_lists = []
        for element in csv_list:
            csv_dict = {}
            for idx in enumerate(element):
                csv_dict[list_keys[idx[0]]] = int(idx[1])
            list_lists.append(csv_dict)

        list_ins = []
        for index in range(len(list_lists)):
            list_ins.append(cls.create(**list_lists[index]))

        return list_ins
