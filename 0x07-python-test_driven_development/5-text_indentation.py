#!/usr/bin/python3
"""

    Write a function that prints a text with 2 new lines

    after each of these characters: ., ? and :

    4. Text indentation

    Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

"""


def text_indentation(text):
    """

        indents a text using the 3 fields
        ., ?, and :

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    modtext = ""
    skip = True
    for char in text:
        if skip == True and char == ' ':
            continue
        elif skip == True and char != ' ':
            skip = False
        modtext += char
        if char in ['.', '?', ':']:
            modtext += "\n\n"
            skip = True
    while True:
        if modtext == "":
            break
        elif modtext[-1] == ' ':
            modtext = modtext[0:-1]
        else:
            break
    print(modtext, end="")
