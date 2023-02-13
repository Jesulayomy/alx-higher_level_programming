#!/usr/bin/python3
""" This module contains unittests for rectangle class """


import sys
import unittest
from io import StringIO
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
