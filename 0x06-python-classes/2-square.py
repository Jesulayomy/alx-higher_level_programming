#!/usr/bin/python3
""" Initializes with size"""


class Square:
    """Square Doc"""

    def __init__(self, size=0):
        """Initializes size as a private attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
