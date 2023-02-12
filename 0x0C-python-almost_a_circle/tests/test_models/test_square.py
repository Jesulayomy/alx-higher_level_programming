#!/usr/bin/python3
""" Unittests for square module """


import sys
import unittest
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareClassMethods(unittest.TestCase):
    """ Test cases for square attributes and methods """

    def setUp(self):
        """ Prerequisite function that sets default parameters """

        Base._Base__nb_objects = 0

    def test_L_Square_min(self):
        """ test default square """

        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_L_Square_full(self):
        """ test default square """

        s2 = Square(2, 1, 2, 501)
        self.assertEqual(s2.width, s2.height)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 501)

    def test_L_Square_empty(self):
        """ test default square """

        with self.assertRaises(TypeError):
            s3 = Square()

    def test_L_Square_str(self):
        """ Test the __str__ method """

        s4 = Square(1)
        self.assertEqual(s4.__str__(), "[Square] (1) 0/0 - 1")
