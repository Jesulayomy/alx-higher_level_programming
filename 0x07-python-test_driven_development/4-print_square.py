#!/usr/bin/python3
"""

    Module for a function that prints a square

    3. Print square

    Write a function that prints a square with the character #.

"""


def print_square(size):
    """

        Prints a square of l and b = size

        size must be an integer or a float

    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        print('#' * size)
