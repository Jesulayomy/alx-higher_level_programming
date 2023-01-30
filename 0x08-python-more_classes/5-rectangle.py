#!/usr/bin/python3
"""
    This module defines a class: Rectangle based on
    0-rectangle. with private attrivutes and instances
"""


class Rectangle:
    """
        1. Real definition of a rectangle
        Write a class Rectangle that defines a rectangle by:
        (based on 0-rectangle.py)
        - Private instance attribute: width:
            property def width(self): to retrieve it
            property setter def width(self, value):
        - Private instance attribute: height:
            property def height(self): to retrieve it
            property setter def height(self, value): to set it:
    """

    def __init__(self, width=0, height=0):
        """

            Initialization or optional Instantiation

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """

            Returns the width

        """

        return self.__width

    @width.setter
    def width(self, value):
        """

            sets the width

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """

            Returns the height

        """

        return self.__height

    @height.setter
    def height(self, value):
        """

            sets the width

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """

            Public instance method: def area(self): that returns

            the rectangle area

        """

        return self.width * self.height

    def perimeter(self):
        """

            Public instance method: def perimeter(self):
            that returns the rectangle perimeter:

                if width or height is equal to 0, perimeter is equal to 0

        """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """

            This method returns the rectangle

            in # values (str of the rectangle)

        """

        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += '#' * self.width + '\n'

        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """

            Method that returns the string represantion of the instance

            Returns - Rectangle(width, height)

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """

            Method that returns the string when an instance is deleted

        """

        print("Bye rectengle...")
