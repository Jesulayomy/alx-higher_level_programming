#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    index = 0
    for char in str:
        if index != n:
            newstr += char
        index += 1
    return newstr
