#!/usr/bin/python3
"""
    This module contains the rectangle class which is a child
    of Base class
"""


from models.base import Base


class Rectangle(Base):
    """
        A child of Base
        Private instance attributes, each with
        its own public getter and setter:

        __width -> width
        __height -> height
        __x -> x
        __y -> y
        Class constructor:
            def __init__(self, width, height, x=0, y=0, id=None)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes the class """

        super().__init__(id)
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(width) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ Width getter """

        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the private instance """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ height getter """

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the private instance """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ height getter """

        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the height of the private instance """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ height getter """

        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the height of the private instance """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ returns teh area of the rectangle """

        return self.__width * self.__height

    def display(self):
        """
            Displays a graphic of the triangle using hashes
            x and y act as offsets
        """

        shape = ""
        if self.__width == 0 or self.__height == 0:
            return shape

        for j in range(self.__y):
            shape += '\n'
        for i in range(self.__height):
            shape += ' ' * self.__x + '#' * self.__width + '\n'

        shape = shape[:-1]
        print(shape)

    def __str__(self):
        """ Overrides the default str method """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height
                )

    def update(self, *args, **kwargs):
        """ assigns args to the variables """

        if args is not None and len(args) != 0:
            list_instance = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_instance[i], args[i])
        else:
            for instance, value in kwargs.items():
                setattr(self, instance, value)

    def to_dictionary(self):
        """ Returns the dict reporesentation of attributes """

        list_instance = ['id', 'width', 'height', 'x', 'y']
        rep = {}
        for key in list_instance:
            rep[key] = getattr(self, key)
        return rep
