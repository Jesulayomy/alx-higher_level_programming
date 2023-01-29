#!/usr/bin/python3
"""

    This modules prints a name in a given format

    2. Say my name

    Write a function that prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """

        This function checs the format and prints

        a first anf last naem using .format

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
