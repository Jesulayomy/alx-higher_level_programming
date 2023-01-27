#!/usr/bin/python3
"""
    Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        indents a text using the 3 fields
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        modtext = ""
        skip = False
        for char in text:
            if skip == True and char == ' ':
                continue
            elif skip == True and char != ' ':
                skip = False
            modtext += char
            if char in ['.', '?', ':']:
                modtext += "\n\n"
                skip = True
        print(modtext, end="")
