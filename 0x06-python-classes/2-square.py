#!/usr/bin/python3
""" Initializes with size"""


class Square:
    """Square Doc"""

    def __init__(self, size=0):
        """Initializes size as a private attribute"""
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                try:
                    self.__size = size
                except TypeError("size must be an integer"):
                    pass
