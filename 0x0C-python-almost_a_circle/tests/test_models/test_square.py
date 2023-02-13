#!/usr/bin/python3
""" Unittests for square module """


import sys
import unittest
from io import StringIO
from models.base import Base
from unittest.mock import patch
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
        self.assertEqual(r2.height, 3)
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

    def test_L_Square_blank(self):
        """ test blanks err """

        with self.assertRaises(TypeError):
            r20 = Square(None)

        r17 = Square(size=4, id=206)
        self.assertEqual(r17.x, 0)
        self.assertEqual(r17.y, 0)

        r16 = Square(5)
        self.assertEqual(r16.width, 5)
        self.assertEqual(r16.height, 5)
        self.assertEqual(r16.x, 0)
        self.assertEqual(r16.y, 0)
        self.assertEqual(r16.id, 2)

    def test_L_Square_5_area(self):
        """ test areas """

        r18 = Square(3, 0, 0, 207)
        self.assertEqual(r18.area(), 9)

        r19 = Square(9)
        self.assertEqual(r19.area(), 81)

    def test_L_Square_6_display(self):
        """ test display """

        subout = StringIO()
        sys.stdout = subout
        r21 = Square(3, 0, 0, 301)
        r21.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(subout.getvalue(), "###\n###\n###\n")

        subout2 = StringIO()
        sys.stdout = subout2
        r22 = Square(3, 1, 1, 302)
        r22.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(subout2.getvalue(), "\n ###\n ###\n ###\n")

    def test_L_Square_7_str(self):
        """ test str """

        r23 = Square(4, 1, 2, 303)
        self.assertEqual(r23.__str__(), "[Square] (303) 1/2 - 4")

    def test_L_Square_8_update(self):
        """ test update """

        r24 = Square(6, 0, 0, 304)
        r24.update(305, 4, 2, 1)
        self.assertEqual(r24.id, 305)
        self.assertEqual(r24.width, 4)
        self.assertEqual(r24.height, 4)
        self.assertEqual(r24.x, 2)
        self.assertEqual(r24.y, 1)

    def test_L_Square_9_bad_updates(self):
        """ test update """

        r24 = Square(6, 0, 0, 304)
        with self.assertRaises(TypeError):
            r24.update(305, "14", 2, 1)

    def test_L_Square_9_update_args(self):
        """ test update """

        r25 = Square(6, 0, 0, 304)
        r25.update(307)
        self.assertEqual(r25.id, 307)

    def test_L_Square_10_no_update_args(self):
        """ test update """

        r24 = Square(6, 0, 0, 304)
        r24.update()
        self.assertEqual(r24.width, 6)
        r24.update("4")
        self.assertEqual(r24.width, 6)

    def test_L_Square_11_update_kargs(self):
        """ test update """

        r27 = Square(6, 0, 0, 304)
        r27.update(id=310, size=4, x=1, y=1)
        self.assertEqual(r27.id, 310)
        self.assertEqual(r27.width, 4)
        self.assertEqual(r27.height, 4)
        self.assertEqual(r27.x, 1)
        self.assertEqual(r27.y, 1)

    def test_L_Square_12_update_kargs_some(self):
        """ test update """

        r27 = Square(6, 0, 0, 304)
        r27.update(id=311, x=1, y=1)
        self.assertEqual(r27.id, 311)
        self.assertEqual(r27.width, 6)
        self.assertEqual(r27.height, 6)
        self.assertEqual(r27.x, 1)
        self.assertEqual(r27.y, 1)

    def test_L_Square_13_dictionary(self):
        """ Test the dictionary representation of the square """

        r28 = Square(3)
        dict_rep = r28.to_dictionary()
        self.assertEqual(
                dict_rep,
                {'id': 1, 'size': 3, 'x': 0, 'y': 0}
                )

    def test_L_Square_13_dictionary_full(self):
        """ Test the dictionary representation of the square """

        r28 = Square(3, 1, 1, 3)
        dict_rep = r28.to_dictionary()
        self.assertEqual(
                dict_rep,
                {'id': 3, 'size': 3, 'x': 1, 'y': 1}
                )

    def test_new_square(self):
        """ Test new square """

        new = Square(1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Test new square with all attrs """

        new = Square(2, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ Test new squares """

        new = Square(1)
        new2 = Square(1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Square is a Base instance """

        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with 1 arg passed """

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
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(1, -1, 1)

    def test_area(self):
        """ Checking the return value of area method """

        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_area_2(self):
        """ Checking the return value of area method """

        new = Square(2, 2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.assertEqual(new.area(), 25)
        new.size = 3
        self.assertEqual(new.area(), 9)

    def test_new_square(self):
        """ Test new square """

        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_2(self):
        """ Test new square with all attrs """

        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
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

        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """

        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with no args passed """

        with self.assertRaises(TypeError):
            new = Square()

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """

        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """

        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """

        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """

        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """

        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Square(1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """

        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_load_from_file(self):
        """ Test load JSON file """

        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_area_2(self):
        """ Checking the return value of area method """

        new = Square(2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.assertEqual(new.area(), 25)

    def test_display(self):
        """ Test string printed """

        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """

        r1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """

        r1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Test __str__ return value """

        r1 = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Test __str__ return value """

        s1 = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s2 = Square(3, 7, 1)
        res = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """

        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3"
        self.assertEqual(s1.__str__(), res)

    def test_display_3(self):
        """ Test string printed """

        s1 = Square(5, 2, 1)
        res = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test string printed """

        s1 = Square(3)
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.x = 1
        res = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.y = 2
        res = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_update(self):
        """ Test update method """

        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_2(self):
        """ Test update method """

        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_3(self):
        """ Test update method """

        s1 = Square(1)
        res = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(y=3)
        res = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(id=1, size=10)
        res = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_4(self):
        """ Test update method """

        s1 = Square(10)
        res = "[Square] (1) 0/0 - 10\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'size': 3, 'y': 5}
        s1.update(**dic)
        res = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_5(self):
        """ Test update method """

        s1 = Square(7)
        res = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'id': 10, 'x': '5', 'y': 5}

        with self.assertRaises(TypeError):
            s1.update(**dic)

    def test_to_dictionary(self):
        """ Test dictionary returned """

        s1 = Square(1, 2, 3)
        res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """

        s1 = Square(2, 2, 2)
        res = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s2 = Square(5)
        res = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)

        self.assertEqual(s1.width, s2.width)
        self.assertEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """

        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_json_file(self):
        """ Test Dictionary to JSON string """

        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res)

        Square.save_to_file([s1])
        res = "[{}]".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with open("Square.json", "r") as file:
            res2 = file.read()

        self.assertEqual(res, res2)

    def test_value_square(self):
        """ Test value pased to Square """

        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_create(self):
        """ Test create method """

        dictionary = {'id': 89}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        """ Test create method """

        dictionary = {'id': 89, 'size': 1}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """ Test create method """

        dictionary = {'id': 89, 'size': 1, 'x': 2}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """

        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """

        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
