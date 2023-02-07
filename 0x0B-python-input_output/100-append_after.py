#!/usr/bin/python3
"""
    Write a function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
        reads the file(filename) and inserts(new_string)
        after every line where search_string is found
    """

    with open(filename, 'r', encoding="utf-8") as fid:
        content = ""
        for line in fid:
            if line.find(search_string) >= 0:
                content += line
                content += new_string
            else:
                content += line

    with open(filename, 'w', encoding="utf-8") as fid:
        fid.write(content)
