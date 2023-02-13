#!/usr/bin/python3
""" This module contains unittests for rectangle class """


import io
import sys
import json
import unittest
from io import StringIO
from pathlib import Path
from models.base import Base
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangleClassMethods(unittest.TestCase):
    """ Tests the rectangle class """

    def setUp(self):
        """ Setup parameters run for each test """

        Base._Base__nb_objects = 0

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

    def test_L_Rectangle_sample(self):
        """ full rectangle sample """

        r1 = Rectangle(2, 4, 2, 1, 12)

        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

    def test_L_Rectangle_excess(self):
        """ tests more attributes than needed """

        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, 0, 0, 201, 7)

    def test_L_Rectangle_no_id(self):
        """ tests without id """

        r2 = Rectangle(3, 5, 3, 2)

        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 2)

    def test_L_Rectangle_no_width(self):
        """ tests without width """

        with self.assertRaises(TypeError):
            r2 = Rectangle(height=3, x=5, y=3, id=2)

    def test_L_Rectangle_no_height(self):
        """ tests without height """

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, x=5, y=3, id=2)

    def test_L_Rectangle_no_x(self):
        """ tests without x """

        r2 = Rectangle(height=3, width=5, y=3, id=2)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 3)

    def test_L_Rectangle_no_y(self):
        """ tests without y """

        r2 = Rectangle(height=3, width=5, x=3, id=2)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)

    def test_L_Rectangle_negative_id(self):
        """ tests with - id """

        r2 = Rectangle(3, 5, 3, 2, -11)

        self.assertEqual(r2.id, -11)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 2)

    def test_L_Rectangle_bad_width(self):
        """ tests without width """

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=True, height=3, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=31.3, height=3, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width="31", height=3, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=[31], height=3, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=(31,), height=3, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width={'width': 31}, height=3, x=5, y=3, id=2)

    def test_L_Rectangle_bad_height(self):
        """ tests without height """

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=True, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12.2, x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height="12", x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=[12], x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=(12,), x=5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height={'height': 12}, x=5, y=3, id=2)

    def test_L_Rectangle_bad_x(self):
        """ tests without x """

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x="5", y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=5.5, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=True, y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=[5], y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=(5,), y=3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x={'x': 5}, y=3, id=2)

    def test_L_Rectangle_bad_y(self):
        """ tests without y """

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=5, y=3.3, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=5, y="3", id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=5, y=True, id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=5, y=[3], id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=5, y=(3,), id=2)

        with self.assertRaises(TypeError):
            r2 = Rectangle(width=3, height=12, x=5, y={'y': 3}, id=2)

    def test_L_Rectangle_bad_value_width(self):
        """ tests with - width """

        with self.assertRaises(ValueError):
            r3 = Rectangle(-1, 4, 2, 1, 101)

    def test_L_Rectangle_bad_value_height(self):
        """ tests with - height """

        with self.assertRaises(ValueError):
            r4 = Rectangle(1, -4, 2, 1, 102)

    def test_L_Rectangle_bad_value_x(self):
        """ tests with - x """

        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 4, -2, 1, 103)

    def test_L_Rectangle_bad_value_y(self):
        """ tests with - y """

        with self.assertRaises(ValueError):
            r6 = Rectangle(1, 4, 2, -1, 104)

    def test_L_Rectangle_blank(self):
        """ test blanks err """

        with self.assertRaises(TypeError):
            r20 = Rectangle(None)

        r17 = Rectangle(width=7, height=4, id=206)
        self.assertEqual(r17.x, 0)
        self.assertEqual(r17.y, 0)

        r16 = Rectangle(5, 3)
        self.assertEqual(r16.width, 5)
        self.assertEqual(r16.height, 3)
        self.assertEqual(r16.x, 0)
        self.assertEqual(r16.y, 0)
        self.assertEqual(r16.id, 1)

    def test_L_Rectangle_5_area(self):
        """ test areas """

        r18 = Rectangle(3, 6, 0, 0, 207)
        self.assertEqual(r18.area(), 18)

        r19 = Rectangle(9, 4)
        self.assertEqual(r19.area(), 36)

    def test_L_Rectangle_6_display(self):
        """ test display """

        subout = StringIO()
        sys.stdout = subout
        r21 = Rectangle(3, 3, 0, 0, 301)
        r21.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(subout.getvalue(), "###\n###\n###\n")

        subout2 = StringIO()
        sys.stdout = subout2
        r22 = Rectangle(3, 3, 1, 1, 302)
        r22.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(subout2.getvalue(), "\n ###\n ###\n ###\n")

    def test_L_Rectangle_7_str(self):
        """ test str """

        r23 = Rectangle(4, 7, 1, 2, 303)
        self.assertEqual(r23.__str__(), "[Rectangle] (303) 1/2 - 4/7")

    def test_L_Rectangle_8_update(self):
        """ test update """

        r24 = Rectangle(6, 2, 0, 0, 304)
        r24.update(305, 4, 1, 2, 1)
        self.assertEqual(r24.id, 305)
        self.assertEqual(r24.width, 4)
        self.assertEqual(r24.height, 1)
        self.assertEqual(r24.x, 2)
        self.assertEqual(r24.y, 1)

    def test_L_Rectangle_9_bad_updates(self):
        """ test update """

        r24 = Rectangle(6, 2, 0, 0, 304)
        with self.assertRaises(TypeError):
            r24.update(305, "14", 1, 2, 1)

    def test_L_Rectangle_9_update_args(self):
        """ test update """

        r25 = Rectangle(6, 2, 0, 0, 304)
        r25.update(307)
        self.assertEqual(r25.id, 307)

    def test_L_Rectangle_10_no_update_args(self):
        """ test update """

        r24 = Rectangle(6, 2, 0, 0, 304)
        r24.update()
        self.assertEqual(r24.width, 6)
        r24.update("4")
        self.assertEqual(r24.width, 6)

    def test_L_Rectangle_11_update_kargs(self):
        """ test update """

        r27 = Rectangle(6, 2, 0, 0, 304)
        r27.update(id=310, width=4, height=4, x=1, y=1)
        self.assertEqual(r27.id, 310)
        self.assertEqual(r27.width, 4)
        self.assertEqual(r27.height, 4)
        self.assertEqual(r27.x, 1)
        self.assertEqual(r27.y, 1)

    def test_L_Rectangle_12_update_kargs_some(self):
        """ test update """

        r27 = Rectangle(6, 2, 0, 0, 304)
        r27.update(id=311, x=1, y=1)
        self.assertEqual(r27.id, 311)
        self.assertEqual(r27.width, 6)
        self.assertEqual(r27.height, 2)
        self.assertEqual(r27.x, 1)
        self.assertEqual(r27.y, 1)

    def test_L_Rectangle_13_dictionary(self):
        """ Test the dictionary representation of the rectangle """

        r28 = Rectangle(3, 2)
        dict_rep = r28.to_dictionary()
        self.assertEqual(
                dict_rep,
                {'id': 1, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
                )

    def test_L_Rectangle_13_dictionary_full(self):
        """ Test the dictionary representation of the rectangle """

        r28 = Rectangle(3, 2, 1, 1, 3)
        dict_rep = r28.to_dictionary()
        self.assertEqual(
                dict_rep,
                {'id': 3, 'width': 3, 'height': 2, 'x': 1, 'y': 1}
                )

    def test_new_rectangle(self):
        """ Test new rectangle """

        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
        """ Test new rectangle with all attrs """

        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ Test new rectangles """

        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Rectangle is a Base instance """

        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """ Test error raise with 1 arg passed """

        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """

        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """

        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """

        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """

        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """

        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_valide_attrs(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """

        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_area_2(self):
        """ Checking the return value of area method """

        new = Rectangle(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """ Checking the return value of area method """

        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.width = 7
        r1.height = 15
        res = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Test __str__ return value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_display_3(self):
        """ Test string printed """
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test string printed """
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_rect(self):
        """ test normal rect"""

        r1 = Rectangle(10, 5, 7, 2, 5)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 5)

    def test_rect2(self):
        """ test normal rect """

        r1 = Rectangle(1, 1)

        r1.id = 5
        self.assertEqual(r1.id, 5)
        r1.height = 10
        self.assertEqual(r1.height, 10)
        r1.width = 3
        self.assertEqual(r1.width, 3)
        r1.x = 4
        self.assertEqual(r1.x, 4)
        r1.y = 2
        self.assertEqual(r1.y, 2)

    def test_rect_no_id(self):
        """ test rect without id """

        r1 = Rectangle(5, 17, 9, 15)

        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 17)
        self.assertEqual(r1.x, 9)
        self.assertEqual(r1.y, 15)
        self.assertEqual(r1.id, 1)

    def test_rect_no_y(self):
        """ test rect without y """

        r1 = Rectangle(200, 10, 17)

        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 17)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_rect_invalid_y1(self):
        """ test rect with wrong y """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(200, 10, 17, "s")
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 5, 20, True)
        with self.assertRaises(TypeError):
            r3 = Rectangle(15, 20, 25, {"y": 1})
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 1, 1, [1, 2])
        with self.assertRaises(TypeError):
            r5.y = "hello"
        with self.assertRaises(TypeError):
            r5.y = {"y": 1}
        with self.assertRaises(TypeError):
            r5.y = (2, 3)
        with self.assertRaises(TypeError):
            r5.y = True

    def test_rect_invalid_y2(self):
        """ test rect with wrong y """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(200, 10, 17, -5)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 5, 20, -10)
        with self.assertRaises(ValueError):
            r5.y = -2
        with self.assertRaises(ValueError):
            r5.y = -100000

    def test_rect_no_x(self):
        """ test rect without x """

        r1 = Rectangle(20, 117)

        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 117)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_rect_invalid_x1(self):
        """ test rect with wrong x """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(200, 10, "hello", 17)
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 5, False, 12)
        with self.assertRaises(TypeError):
            r3 = Rectangle(15, 20, {"y": 1})
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 1, [1], 20)
        with self.assertRaises(TypeError):
            r5.x = "s"
        with self.assertRaises(TypeError):
            r5.x = {"x": 1}
        with self.assertRaises(TypeError):
            r5.x = (1, 1)
        with self.assertRaises(TypeError):
            r5.x = True

    def test_rect_invalid_x2(self):
        """ test rect with wrong x """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(200, 10, -5, 10)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 5, -10)
        with self.assertRaises(ValueError):
            r5.x = -5
        with self.assertRaises(ValueError):
            r5.x = -256

    def test_rect_no_height(self):
        """ test rect without height """

        with self.assertRaises(TypeError):
            r1 = Rectangle(20)

    def test_rect_invalid_height1(self):
        """ test rect with wrong height """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(200, "s", 10, 20)
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, False, 0)
        with self.assertRaises(TypeError):
            r3 = Rectangle(15, {"y": 1}, 25)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, [1, 2], 0, 0)
        with self.assertRaises(TypeError):
            r5.height = "hello"
        with self.assertRaises(TypeError):
            r5.height = {"y": 1}
        with self.assertRaises(TypeError):
            r5.height = (17, 5)
        with self.assertRaises(TypeError):
            r5.height = True

    def test_rect_invalid_height2(self):
        """ test rect with wrong height """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(200, -5, 20)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, -10)
        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            r5.height = -2
        with self.assertRaises(ValueError):
            r5.height = 0
        with self.assertRaises(ValueError):
            r5.height = -500

    def test_rect_no_width(self):
        """ test rect without width """

        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_rect_invalid_width1(self):
        """ test rect with wrong width """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 10, 20)
        with self.assertRaises(TypeError):
            r2 = Rectangle(False, 20)
        with self.assertRaises(TypeError):
            r3 = Rectangle({"y": 1}, 25)
        with self.assertRaises(TypeError):
            r4 = Rectangle([1, 2], 1, 0)
        with self.assertRaises(TypeError):
            r5.width = "hello"
        with self.assertRaises(TypeError):
            r5.width = {"y": 1}
        with self.assertRaises(TypeError):
            r5.width = [1]
        with self.assertRaises(TypeError):
            r5.width = True

    def test_rect_invalid_width2(self):
        """ test rect with wrong width """
        r5 = Rectangle(1, 17, 2, 5)

        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, 20)
        with self.assertRaises(ValueError):
            r2 = Rectangle(-10, 15)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r5.width = -2
        with self.assertRaises(ValueError):
            r5.width = 0
        with self.assertRaises(ValueError):
            r5.width = -500

    def test_rect_more_args(self):
        """ test rect with more args than expected """

        with self.assertRaises(TypeError):
            r1 = Rectangle(12, 2, 0, 0, 1, 17)

    def test_rect_area(self):
        """ test rect area """

        r1 = Rectangle(1, 15)
        self.assertEqual(r1.area(), 15)

        r2 = Rectangle(3, 15)
        self.assertEqual(r2.area(), 45)

        r3 = Rectangle(2, 5)
        self.assertEqual(r3.area(), 10)

        r4 = Rectangle(12, 10)
        self.assertEqual(r4.area(), 120)

        r4.width = 5
        self.assertEqual(r4.area(), 50)

        r4.height = 12
        self.assertEqual(r4.area(), 60)

    def test_rect_area_args(self):
        """ test rect area with args """

        r1 = Rectangle(12, 10)

        with self.assertRaises(TypeError):
            r1.area(12)

    def test_rect_str(self):
        """ test the __str__ method """

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(10, 5)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 0/0 - 10/5")

        r3 = Rectangle(1, 17, 2)
        self.assertEqual(r3.__str__(), "[Rectangle] (2) 2/0 - 1/17")

    def test_rect_str_args(self):
        """ test __str__ method with args """
        r1 = Rectangle(1, 13)

        with self.assertRaises(TypeError):
            r1.__str__("hey")

    def test_rect_display(self):
        """ test the display method """

        r1 = Rectangle(3, 4)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "###\n###\n###\n###\n")

    def test_rect_display2(self):
        """ test the display method """

        r1 = Rectangle(5, 5, 3, 2)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        exp_output = "\n\n   #####\n   #####\n   #####\n   #####\n   #####\n"
        self.assertEqual(output.getvalue(), exp_output)

    def test_rect_display3(self):
        """ test the display method """

        r1 = Rectangle(2, 1, 1, 0)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), " ##\n")

    def test_rect_display4(self):
        """ test the display method """

        r1 = Rectangle(4, 3, 0, 5)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "\n\n\n\n\n####\n####\n####\n")

    def test_rect_display_args(self):
        """ test display with args """

        r1 = Rectangle(2, 4)

        with self.assertRaises(TypeError):
            r1.display([])

    def test_rect_update_args(self):
        """ test rect update with args"""

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(2)
        self.assertEqual(r1.id, 2)

        r1.update(10, 5, 3)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(1, 17, 4, 5, 7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 17)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)

        # update with extra values in args
        r1.update(15, 2, 34, 33, 22, 12, 27)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 34)
        self.assertEqual(r1.x, 33)
        self.assertEqual(r1.y, 22)

        # if args and kwargs is given, args is used
        r1.update(1, 20, 11, 8, 2, height=1, id=5, x=2, y=4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 11)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 2)

    def test_rect_update_invalid_args1(self):
        """ test update with invalid args """

        r1 = Rectangle(16, 12)

        # width errors
        with self.assertRaises(TypeError):
            r1.update(1, "s", 10)
        with self.assertRaises(TypeError):
            r1.update(2, True, 15)
        with self.assertRaises(TypeError):
            r1.update(1, [1], 30)
        with self.assertRaises(TypeError):
            r1.update(2, {"y": 15}, 25)

        # height errors
        with self.assertRaises(TypeError):
            r1.update(13, 20, "hello")
        with self.assertRaises(TypeError):
            r1.update(1, 12, False)
        with self.assertRaises(TypeError):
            r1.update(1, 15, [1])
        with self.assertRaises(TypeError):
            r1.update(1, {"y": 15}, 25)

        # x errors
        with self.assertRaises(TypeError):
            r1.update(12, 20, 15, "13")
        with self.assertRaises(TypeError):
            r1.update(1, 5, 2, False)
        with self.assertRaises(TypeError):
            r1.update(2, 15, 17, [1])
        with self.assertRaises(TypeError):
            r1.update(3, 20, 20, {"y": 15}, 25)

        # y errors
        with self.assertRaises(TypeError):
            r1.update(1, 20, 15, 0, "13")
        with self.assertRaises(TypeError):
            r1.update(2, 5, 2, 12, True)
        with self.assertRaises(TypeError):
            r1.update(3, 15, 17, 1, [1, 2])
        with self.assertRaises(TypeError):
            r1.update(4, 25, 20, 20, {"y": 15}, 25)

    def test_rect_update_invalid_args2(self):
        """ test update with invalid args """

        r1 = Rectangle(16, 12)

        # width errors
        with self.assertRaises(ValueError):
            r1.update(1, -5, 10)
        with self.assertRaises(ValueError):
            r1.update(1, 0, 15)

        # height errors
        with self.assertRaises(ValueError):
            r1.update(1, 13, -2)
        with self.assertRaises(ValueError):
            r1.update(2, 1, 0)

        # x errors
        with self.assertRaises(ValueError):
            r1.update(12, 20, 15, -17)

        # y errors
        with self.assertRaises(ValueError):
            r1.update(2, 15, 2, 0, -20)

    def test_rect_update_kwargs(self):
        """ test update with kwargs """

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(id=10, width=5)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)

        r1.update(height=2, x=17)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 17)
        self.assertEqual(r1.y, 10)

        r1.update(height=13, y=5, x=17, id=2, width=7)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 7)
        self.assertEqual(r1.height, 13)
        self.assertEqual(r1.x, 17)
        self.assertEqual(r1.y, 5)

    def test_rect_update_invalid_kwargs1(self):
        """ test update with invalid kwargs """

        r1 = Rectangle(16, 12)
        invalid_t = ["s", (1, 2), True, False, "65", [1], {"w": 5}]

        # width errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(width=typ, id=1)

        # height errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(height=typ)

        # x errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(x=typ, width=2, height=15)

        # y errors
        for typ in invalid_t:
            with self.assertRaises(TypeError):
                r1.update(x=0, y=typ)

    def test_update_invalid_kwargs2(self):
        """ test update with invalid kwargs """

        r1 = Rectangle(16, 12)

        # width errors
        with self.assertRaises(ValueError):
            r1.update(width=-5)
        with self.assertRaises(ValueError):
            r1.update(width=0, id=3)

        # height errors
        with self.assertRaises(ValueError):
            r1.update(height=-2)
        with self.assertRaises(ValueError):
            r1.update(x=0, width=20, height=0)

        # x errors
        with self.assertRaises(ValueError):
            r1.update(id=5, x=-17)

        # y errors
        with self.assertRaises(ValueError):
            r1.update(y=-20)

    def test_rect_update_less_args(self):
        """ test update method with less args """

        r1 = Rectangle(12, 3)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        # when update is called with no args, rect does not change
        r1.update()

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rect_to_dictionary(self):
        """ test the to_dictionary method """

        r1 = Rectangle(10, 2, 1, 2, 5)
        dict_r1 = r1.to_dictionary()
        self.assertEqual(dict_r1["id"], 5)
        self.assertEqual(dict_r1["x"], 1)
        self.assertEqual(dict_r1["y"], 2)
        self.assertEqual(dict_r1["width"], 10)
        self.assertEqual(dict_r1["height"], 2)

        r1.update(1, 5, 13)
        dict_r1 = r1.to_dictionary()
        self.assertEqual(dict_r1["id"], 1)
        self.assertEqual(dict_r1["x"], 1)
        self.assertEqual(dict_r1["y"], 2)
        self.assertEqual(dict_r1["width"], 5)
        self.assertEqual(dict_r1["height"], 13)

    def test_rect_to_dictionary_err(self):
        """ test to_dictionary with error """

        r1 = Rectangle(12, 5)
        dict_r1 = r1.to_dictionary()

        with self.assertRaises(KeyError):
            dict_r1["size"]

    def test_rect_to_dictionary_args(self):
        """ test to_dictionary method with args """

        r1 = Rectangle(10, 4)

        with self.assertRaises(TypeError):
            dict_r1 = r1.to_dictionary(1)

    def test_rect_save_to_file(self):
        """ test the save to file method """

        r1 = Rectangle(5, 6)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        rect_list = [r1.to_dictionary(), r2.to_dictionary()]
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), json.dumps(rect_list))

    def test_rect_save_to_file2(self):
        """ test the save to file method """

        r1 = Rectangle(2, 5, 3)
        Rectangle.save_to_file([r1])

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), json.dumps([r1.to_dictionary()]))

    def test_rect_save_to_file3(self):
        """ test the save to file method """

        r1 = Rectangle(2, 5, 3)
        r2 = Rectangle(2, 4, 1, 1)
        r3 = Rectangle(4, 5)
        Rectangle.save_to_file([r1, r2, r3])

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        rect_list = [
            r1.to_dictionary(),
            r2.to_dictionary(),
            r3.to_dictionary()
        ]
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), json.dumps(rect_list))

    def test_rect_save_to_file_none(self):
        """ test the save to file method with none """

        Rectangle.save_to_file(None)

        rect_file = Path("Rectangle.json")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_rect_save_to_file_more_args(self):
        """  test save to file with more args than expected """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 3)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([r1], [r2])

    def test_rect_save_to_file_less_args(self):
        """ test save to file with less args """

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_rect_create(self):
        """ test the create method """

        obj_dict = {"id": 2, "width": 3, "height": 5, "x": 2}
        r1 = Rectangle.create(**obj_dict)

        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 2)
        r2_dict = r2.to_dictionary()
        r3 = Rectangle.create(**r2_dict)

        self.assertFalse(r2 is r3)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_rect_create_no_args(self):
        """ test create method with no args """

        r1 = Rectangle.create()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rect_load_from_file(self):
        """ test the load_from_file method """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        rect_list = [r1, r2]

        Rectangle.save_to_file(rect_list)
        rect_list_output = Rectangle.load_from_file()

        self.assertTrue(rect_list_output[0] is not r1)
        self.assertTrue(rect_list_output[1] is not r2)

        for i in range(2):
            self.assertEqual(rect_list_output[i].id, rect_list[i].id)
            self.assertEqual(rect_list_output[i].height, rect_list[i].height)
            self.assertEqual(rect_list_output[i].width, rect_list[i].width)
            self.assertEqual(rect_list_output[i].x, rect_list[i].x)
            self.assertEqual(rect_list_output[i].y, rect_list[i].y)

    def test_rect_load_from_file_args(self):
        """ test the load from file method with args """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(5, 2)
        rect_list = [r1, r2]

        Rectangle.save_to_file(rect_list)

        with self.assertRaises(TypeError):
            list_output = Rectangle.load_from_file(3)

    def test_rect_save_to_file_csv(self):
        """ test the save to file csv method """

        r1 = Rectangle(5, 6)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file_csv([r1, r2])

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        exp_str = "1,5,6,0,0\n2,2,4,1,1\n"
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), exp_str)

    def test_rect_save_to_file_csv2(self):
        """ test the save to file csv method """

        r1 = Rectangle(2, 5, 3)
        Rectangle.save_to_file_csv([r1])

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), "1,2,5,3,0\n")

    def test_rect_save_to_file_csv3(self):
        """ test the save to file csv method """

        r1 = Rectangle(2, 5, 3)
        r2 = Rectangle(2, 4, 1, 1)
        r3 = Rectangle(4, 5)
        Rectangle.save_to_file_csv([r1, r2, r3])

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        exp_str = "1,2,5,3,0\n2,2,4,1,1\n3,4,5,0,0\n"
        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), exp_str)

    def test_rect_save_to_file_csv_none(self):
        """ test the save to file csv method with none """

        Rectangle.save_to_file_csv(None)

        rect_file = Path("Rectangle.csv")
        self.assertTrue(rect_file.is_file())

        with open(rect_file, "r") as f:
            self.assertEqual(f.read(), '')

    def test_rect_save_to_file_csv_more_args(self):
        """  test save to file csv with more args than expected """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 3)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([r1], [r2])

    def test_rect_save_to_file_less_args(self):
        """ test save to file with less args """

        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_rect_load_from_file_csv(self):
        """ test the load_from_file_csv method """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        rect_list = [r1, r2]

        Rectangle.save_to_file_csv(rect_list)
        rect_list_output = Rectangle.load_from_file_csv()

        self.assertTrue(rect_list_output[0] is not r1)
        self.assertTrue(rect_list_output[1] is not r2)

        for i in range(2):
            self.assertEqual(rect_list_output[i].id, rect_list[i].id)
            self.assertEqual(rect_list_output[i].height, rect_list[i].height)
            self.assertEqual(rect_list_output[i].width, rect_list[i].width)
            self.assertEqual(rect_list_output[i].x, rect_list[i].x)
            self.assertEqual(rect_list_output[i].y, rect_list[i].y)

    def test_rect_load_from_file_csv_args(self):
        """ test the load from file csv method with args """

        r1 = Rectangle(2, 3)
        r2 = Rectangle(5, 2)
        rect_list = [r1, r2]

        Rectangle.save_to_file_csv(rect_list)

        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv(rect_list)
