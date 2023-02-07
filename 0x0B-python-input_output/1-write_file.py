#!/usr/bin/python3
"""
    The module finction writes to a file, replacing its contents
"""


def write_file(filename="", text=""):
    """
        Writes to the file named filename and overites existing content
    """

    with open(filename, 'w', encoding="utf-8") as fid:
        chars_no = fid.write(text)
    return chars_no
