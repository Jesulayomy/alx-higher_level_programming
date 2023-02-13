#!/usr/bin/python3
"""
    This module contains the square class, son of rectangle, son of base
    collects its methods (init)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        A grandchild of base and child of rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes squares
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Width/height getter """

        return self.width

    @size.setter
    def size(self, value):
        """ Sets the width/height of the private instance """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
            Overrides the default str, and the one in rect
        """

        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    def update(self, *args, **kwargs):
        """
            Assignes values based on arguments provided
        """

        if args is not None and len(args) != 0:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attributes[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attributes[i], args[i])
        else:
            for name, value in kwargs.items():
                if name == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, name, value)

    def to_dictionary(self):
        """ Dict for square class """

        attributes = ['id', 'size', 'x', 'y']
        rep = {}
        for key in attributes:
            if key == 'size':
                rep[key] = getattr(self, 'width')
            else:
                rep[key] = getattr(self, key)

        return rep
