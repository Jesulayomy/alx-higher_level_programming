#!/usr/bin/python3
""" This module contains unittests for base class """


import sys
import unittest
from io import StringIO
from models.base import Base


class TestBaseClassMethods(unittest.TestCase):
    """
        Tests the base class
        NB: id is always an integer, so no need to test
        other types
    """

    def setUp(self):
        """ Runs for every test """

        Base._Base__nb_objects = 0

    def test_L_base_empty(self):
        """
            Base id tests
            - No value
        """

        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_L_base_negative(self):
        """
            Base id tests
            - Negative value
        """

        b2 = Base(-1)
        self.assertEqual(b2.id, -1)

    def test_L_base_positive(self):
        """
            Base id tests
            - Positive value
        """

        b3 = Base(7)
        self.assertEqual(b3.id, 7)

    def test_L_base_zero(self):
        """
            Base id tests
            - zero
        """

        b4 = Base(0)
        self.assertEqual(b4.id, 0)

    def test_L_base_none(self):
        """
            Base id tests
            - None
        """

        b5 = Base(None)
        self.assertEqual(b5.id, 1)

    def test_L_base_excess(self):
        """ Passinf more than needed """

        with self.assertRaises(TypeError):
            b6 = Base(6, 9)

    def test_L_base_private(self):
        """ Requaesting private attributes """

        b7 = Base()
        with self.assertRaises(AttributeError):
            b7.__nb_objects
