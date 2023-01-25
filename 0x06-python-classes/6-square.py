#!/usr/bin/python3
""" Initializes with size"""


class Square:
    """Square Docstring"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes size and position as a private attribute"""
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[1] < 0 or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        self.__size = size

    def area(self):
        """Returns the area of the square object/instance"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the size private attribute"""
        return self.__size

    @property
    def position(self):
        """Retrieves the position private attribute"""
        return self.__position

    @size.setter
    def size(self, value=0):
        """Sets the size of the current attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value=(0, 0)):
        """Sets the size of the current attribute"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or value[0] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square with # character"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.position[0], end="")
                print('#' * self.__size)
