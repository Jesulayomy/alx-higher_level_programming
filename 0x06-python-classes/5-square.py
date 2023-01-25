#!/usr/bin/python3
""" Initializes with size"""


class Square:
    """Square Docstring"""

    def __init__(self, size=0):
        """Initializes size as a private attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square object/instance"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the size private attribute"""
        return self.__size

    @size.setter
    def size(self, value=0):
        """Sets the size of the current attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square with # character"""
        for range(0, size):
            print('#' * size)
        print()
