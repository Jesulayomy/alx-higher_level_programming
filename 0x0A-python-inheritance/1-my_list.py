#!/usr/bin/python3
"""
    This module contains a child of the class list
    This class has a method print_sorted() that prints out the
    elements of the list in sorted order
"""


class MyList(list):
    """
        A class with parent: list
    """

    def print_sorted(self):
        """
            Prints out the list in sorted order
        """

        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
