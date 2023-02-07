#!/usr/bin/python3
"""
    defines a student class with attributes and methods
"""


class Student:
    """
        This class contains some public attributes and methods
    """

    def __init__(self, first_name, last_name, age):
        """
            initialization fuunction
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            retrieves a dictionary representation of a Student instance
            (same as 8-class_to_json.py)
        """

        return (self.__dict__)
