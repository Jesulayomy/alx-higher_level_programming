#!/usr/bin/python3
"""
    The function below appends a test to the end of the file specified
"""


def append_write(filename="", text=""):
    """
        Appends text to filename
    """

    with open(filename, 'a', encoding="utf-8") as fid:
        chars_no = fid.write(text)
    return chars_no
