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

    def test_L_Square_no_id(self):
        """ tests without id """

        r2 = Square(3, 3, 2)

        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 2)

    def test_L_Square_empty(self):
        """ test default square """

        with self.assertRaises(TypeError):
            s3 = Square()

    def test_L_Square_excess(self):
        """ tests more attributes than needed """

        with self.assertRaises(TypeError):
            r2 = Square(2, 2, 0, 0, 201, 7)

    def test_L_Square_str(self):
        """ Test the __str__ method """

        s4 = Square(1)
        self.assertEqual(s4.__str__(), "[Square] (1) 0/0 - 1")

    def test_L_Square_no_x(self):
        """ tests without x """

        r2 = Square(size=3, y=3, id=2)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 3)

    def test_L_Square_no_y(self):
        """ tests without y """

        r2 = Square(size=5, x=3, id=2)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)

    def test_L_Square_negative_id(self):
        """ tests with - id """

        r2 = Square(3, 3, 2, -11)

        self.assertEqual(r2.id, -11)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 2)

    def test_L_Square_bad_size(self):
        """ tests without width """

        with self.assertRaises(TypeError):
            r2 = Square(size=True, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=1.5, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size="31", x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=[31], x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=(31,), x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size={'size': 31}, x=5, y=3, id=2)

    def test_L_Square_bad_x(self):
        """ tests without x """

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x="5", y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=5.5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=True, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=[5], y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=(5,), y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x={'x': 5}, y=3, id=2)

    def test_L_Square_bad_y(self):
        """ tests without y """

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=5, y=3.3, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=5, y="3", id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=5, y=True, id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=5, y=[3], id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=5, y=(3,), id=2)

        with self.assertRaises(TypeError):
            r2 = Square(size=12, x=5, y={'y': 3}, id=2)

    def test_L_Square_bad_value_size(self):
        """ tests with - width """

        with self.assertRaises(ValueError):
            r3 = Square(-1, 2, 1, 101)

    def test_L_Square_bad_value_x(self):
        """ tests with - x """

        with self.assertRaises(ValueError):
            r5 = Square(1, -2, 1, 103)

    def test_L_Square_bad_value_y(self):
        """ tests with - y """

        with self.assertRaises(ValueError):
            r6 = Square(4, 2, -1, 104)

""" """
    def test_L_Square_blank(self):
        """ test blanks err """

        with self.assertRaises(TypeError):
            r20 = Square(None)

        r17 = Square(width=7, height=4, id=206)
        self.assertEqual(r17.x, 0)
        self.assertEqual(r17.y, 0)

        r16 = Square(5, 3)
        self.assertEqual(r16.width, 5)
        self.assertEqual(r16.height, 3)
        self.assertEqual(r16.x, 0)
        self.assertEqual(r16.y, 0)
        self.assertEqual(r16.id, 1)

    def test_L_Square_5_area(self):
        """ test areas """

        r18 = Square(3, 6, 0, 0, 207)
        self.assertEqual(r18.area(), 18)

        r19 = Square(9, 4)
        self.assertEqual(r19.area(), 36)

    def test_L_Square_6_display(self):
        """ test display """

        subout = StringIO()
        sys.stdout = subout
        r21 = Square(3, 3, 0, 0, 301)
        r21.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(subout.getvalue(), "###\n###\n###\n")

        subout2 = StringIO()
        sys.stdout = subout2
        r22 = Square(3, 3, 1, 1, 302)
        r22.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(subout2.getvalue(), "\n ###\n ###\n ###\n")

    def test_L_Square_7_str(self):
        """ test str """

        r23 = Square(4, 7, 1, 2, 303)
        self.assertEqual(r23.__str__(), "[Square] (303) 1/2 - 4/7")

    def test_L_Square_8_update(self):
        """ test update """

        r24 = Square(6, 2, 0, 0, 304)
        r24.update(305, 4, 1, 2, 1)
        self.assertEqual(r24.id, 305)
        self.assertEqual(r24.width, 4)
        self.assertEqual(r24.height, 1)
        self.assertEqual(r24.x, 2)
        self.assertEqual(r24.y, 1)

    def test_L_Square_9_bad_updates(self):
        """ test update """

        r24 = Square(6, 2, 0, 0, 304)
        with self.assertRaises(TypeError):
            r24.update(305, "14", 1, 2, 1)

    def test_L_Square_9_update_args(self):
        """ test update """

        r25 = Square(6, 2, 0, 0, 304)
        r25.update(307)
        self.assertEqual(r25.id, 307)

    def test_L_Square_10_no_update_args(self):
        """ test update """

        r24 = Square(6, 2, 0, 0, 304)
        r24.update()
        self.assertEqual(r24.width, 6)
        r24.update("4")
        self.assertEqual(r24.width, 6)

    def test_L_Square_11_update_kargs(self):
        """ test update """

        r27 = Square(6, 2, 0, 0, 304)
        r27.update(id=310, width=4, height=4, x=1, y=1)
        self.assertEqual(r27.id, 310)
        self.assertEqual(r27.width, 4)
        self.assertEqual(r27.height, 4)
        self.assertEqual(r27.x, 1)
        self.assertEqual(r27.y, 1)

    def test_L_Square_12_update_kargs_some(self):
        """ test update """

        r27 = Square(6, 2, 0, 0, 304)
        r27.update(id=311, x=1, y=1)
        self.assertEqual(r27.id, 311)
        self.assertEqual(r27.width, 6)
        self.assertEqual(r27.height, 2)
        self.assertEqual(r27.x, 1)
        self.assertEqual(r27.y, 1)

    def test_L_Square_13_dictionary(self):
        """ Test the dictionary representation of the square """

        r28 = Square(3, 2)
        dict_rep = r28.to_dictionary()
        self.assertEqual(
                dict_rep,
                {'id': 1, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
                )

    def test_L_Square_13_dictionary_full(self):
        """ Test the dictionary representation of the square """

        r28 = Square(3, 2, 1, 1, 3)
        dict_rep = r28.to_dictionary()
        self.assertEqual(
                dict_rep,
                {'id': 3, 'width': 3, 'height': 2, 'x': 1, 'y': 1}
                )

    def test_new_square(self):
        """ Test new square """

        new = Square(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Test new square with all attrs """

        new = Square(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ Test new squares """

        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Square is a Base instance """

        new = Square(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with 1 arg passed """

        with self.assertRaises(TypeError):
            new = Square(1)

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """

        with self.assertRaises(TypeError):
            new = Square()

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """

        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """

        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """

        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """

        new = Square(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(0, 1)

    def test_value_attrs_1(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(1, 0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(1, 1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """

        new = Square(4, 5)
        self.assertEqual(new.area(), 20)

    def test_area_2(self):
        """ Checking the return value of area method """

        new = Square(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """ Checking the return value of area method """

        new = Square(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Square(10, 10)
        self.assertEqual(new2.area(), 100)
