#!/usr/bin/python3
"""
    Module returns a lisr opf list for the pascal's triangle of size n
"""


def pascal_triangle(n):
    """
        uses loops to replicate pascal triangle behaviour
    """

    if n <= 0:
        return []
    start = [1, 1]
    result = []
    result += [[1]]
    for i in range(1, n):
        result += [start]
        new = [1]
        for idx in range(len(start) - 1):
            new += [start[idx] + start[idx + 1]]
        new += [1]
        start = new
    return result
