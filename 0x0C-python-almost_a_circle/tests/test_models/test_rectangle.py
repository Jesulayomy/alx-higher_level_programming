#!/usr/bin/python3
""" This module contains unittests for rectangle class """


import unittest
from models.rectangle import Rectangle


class TestRectangleClassMethods(unittest.TestCase):
    """ Tests the rectangle class """

    def setUp(self):
        """ Setup parameters """

        Rectangle._Base__nb_instances = 0

    def test_L_Rectangle_1_sample(self):
        """
            Rectangle id tests
            - all good
            - id cases
            - width cases
            - height cases
            - x cases
            - y cases
            - wrong cases
            - empty cases
        """

        r1 = Rectangle(2, 4, 2, 1, 12)
        r2 = Rectangle(3, 5, 3, 2)

        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 2)

    def test_L_Rectangle_2_value(self):
        """ test valueerr"""

        with self.assertRaises(ValueError):
            r3 = Rectangle(-1, 4, 2, 1, 101)

        with self.assertRaises(ValueError):
            r4 = Rectangle(1, -4, 2, 1, 102)

        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 4, -2, 1, 103)

        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 4, 2, -1, 104)

    def test_L_Rectangle_3_type(self):
        """ test typeserr """

        with self.assertRaises(TypeError):
            r7 = Rectangle("1", 4, 2, 1, 101)

        with self.assertRaises(TypeError):
            r8 = Rectangle(1, (3, 5), 2, 1, 102)

        with self.assertRaises(TypeError):
            r9 = Rectangle(1, 4, [3], 1, 103)

        with self.assertRaises(TypeError):
            r10 = Rectangle(1, 4, 2, 1.235, 104)

    def test_L_Rectangle_4_blanks(self):
        """ test blanks """

        r11 = Rectangle(width=1, height=4, x=2, y=1)
        self.assertEqual(r11.id, 2)

        with self.assertRaises(TypeError):
            r20 = Rectangle(None)

        with self.assertRaises(TypeError):
            r12 = Rectangle(height=4, x=2, y=1)

        with self.assertRaises(TypeError):
            r13 = Rectangle(width=4, x=2, y=1)

        r14 = Rectangle(width=7, height=4, y=1)
        self.assertEqual(r14.x, 0)

        r15 = Rectangle(width=7, height=4, x=1)
        self.assertEqual(r15.y, 0)

        r17 = Rectangle(width=7, height=4, id=206)
        self.assertEqual(r17.x, 0)
        self.assertEqual(r17.y, 0)

        r16 = Rectangle(5, 3)
        self.assertEqual(r16.width, 5)
        self.assertEqual(r16.height, 3)
        self.assertEqual(r16.x, 0)
        self.assertEqual(r16.y, 0)
        self.assertEqual(r16.id, 5)

    def test_L_Rectangle_5_area(self):
        """ test areas """

        r18 = Rectangle(3, 6, 0, 0, 207)
        self.assertEqual(r18.area(), 18)

        r19 = Rectangle(9, 4)
        self.assertEqual(r19.area(), 36)

    def test_L_Rectangle_6_display(self):
        """ test display """

        r21 = Rectangle(3, 3, 0, 0, 301)
        self.assertEqual(r21.display(), print("###\n###\n###\n"))

        r22 = Rectangle(3, 3, 1, 1, 302)
        self.assertEqual(r22.display(), print("\n ###\n ###\n ###\n"))

    def test_L_Rectangle_7_str(self):
        """ test str """

        r23 = Rectangle(4, 7, 1, 2, 303)
        self.assertEqual(print(r23), print("[Rectangle] (303) 1/2 - 4/7"))

    def test_L_Rectangle_8_update(self):
        """ test update """

        r24 = Rectangle(6, 2, 0, 0, 304)
        r24.update(305, 4, 1, 2, 1)
        self.assertEqual(r24.id, 305)
        self.assertEqual(r24.width, 4)
        self.assertEqual(r24.height, 1)
        self.assertEqual(r24.x, 2)
        self.assertEqual(r24.y, 1)
