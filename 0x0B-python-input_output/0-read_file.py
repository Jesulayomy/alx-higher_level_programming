#!/usr/bin/python3
"""
    The module reads a file and prints its contents
"""


def read_file(filename=""):
    """
        Reads the file named filename and prints the contents pf the file
    """

    with open(filename, 'r', encoding="utf-8") as fid:
        print(fid.read(), end="")
