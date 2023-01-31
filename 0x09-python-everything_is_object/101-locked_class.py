#!/usr/bin/python3
"""
    This module contains a locked class that
    prevents the user from externally
    creating new instance attributes except if
    the attribute is "first_name"
"""


class LockedClass:
    """ A locked class that rejects new variables """

    __slots__ = ["first_name"]

    def __init__(self):
        """ Initializes self """

        pass
