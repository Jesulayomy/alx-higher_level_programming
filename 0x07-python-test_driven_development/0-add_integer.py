#!/usr/bin/python3
"""

    This module defines a function that adds two integers

    It also raises errors for appropriate exceptions

"""


def add_integer(a, b=98):
    """

        Adds two integers a and b, b is defaulted to a value

        of 98 and both a and b must be ints or floats

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
