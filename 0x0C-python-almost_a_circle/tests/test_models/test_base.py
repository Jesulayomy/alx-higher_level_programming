#!/usr/bin/python3
""" This module contains unittests for base class """


import unittest
from models.base import Base


class TestBaseClassMethods(unittest.TestCase):
    """ Tests the base class """

    def test_base_sample(self):
        """
            Base id tests
            - No value
            - Negative value
            - Positive value
            - zero
            - None
        """

        b1 = Base()
        b2 = Base(-1)
        b3 = Base(7)
        b4 = Base(0)
        b5 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, -1)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 0)
        self.assertEqual(b5.id, 2)

    def tearDown(self):
        """ disposes variables """

        pass
