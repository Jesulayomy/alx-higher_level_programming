#!/usr/bin/python3
""" This module contains unittests for base class """


import sys
import json
import unittest
from io import StringIO
from models.base import Base
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle


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

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_base_id(self):
        """ test the base class """

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(5)
        self.assertEqual(b2.id, 5)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b5 = Base(None)
        self.assertEqual(b5.id, 3)
        b6 = Base(-10)
        self.assertEqual(b6.id, -10)
        b7 = Base(0)
        self.assertEqual(b7.id, 0)

    def test_base_id_string(self):
        """ test base id with strings """

        b1 = Base("3")
        self.assertEqual(b1.id, "3")
        b2 = Base("1")
        self.assertEqual(b2.id, "1")

    def test_base_id_more_args(self):
        """ test id with more args than expected """

        with self.assertRaises(TypeError):
            b1 = Base(1, 4)

    def test_base_to_json_string(self):
        """ test the to_json_string """

        list_dict = [
            {"id": 1, "height": 5, "width": 4, "x": 0, "y": 0},
            {"id": 2, "height": 15, "width": 5, "x": 2, "y": 0},
            {"id": 3, "height": 5, "width": 4, "x": 4, "y": 2}
        ]

        base_json = Base.to_json_string(list_dict)
        self.assertTrue(type(base_json) is str)
        self.assertEqual(base_json, json.dumps(list_dict))

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")

    def test_base_to_json_string2(self):
        """ test the to_json_string with instances """

        r1 = Rectangle(2, 4)
        r1_list = [r1.to_dictionary()]

        r1_base_json = Base.to_json_string(r1_list)
        self.assertTrue(type(r1_base_json) is str)
        self.assertEqual(r1_base_json, json.dumps(r1_list))

        s1 = Square(4)
        s1_list = [s1.to_dictionary()]

        s1_base_json = Base.to_json_string(s1_list)
        self.assertTrue(type(s1_base_json) is str)
        self.assertTrue(s1_base_json, json.dumps(r1_list))

    def test_base_to_json_string_more_args(self):
        """ test the to_json_string with more args than expected """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.to_json_string([r1.to_dictionary()], [s1.to_dictionary()])

    def test_base_to_json_string_no_args(self):
        """ test the to_json_string with no args """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_base_from_json_string(self):
        """ test the from_json_string """

        list_dict = [
            {"id": 1, "height": 5, "width": 4, "x": 0, "y": 0},
            {"id": 2, "height": 15, "width": 5, "x": 2, "y": 0},
            {"id": 3, "height": 5, "width": 4, "x": 4, "y": 2}
        ]

        base_json = Base.to_json_string(list_dict)
        output = Base.from_json_string(base_json)
        self.assertFalse(type(output) is str)
        self.assertTrue(type(output) is list)
        self.assertEqual(output, json.loads(base_json))

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{}]"), [{}])

    def test_base_from_json_string2(self):
        """ test the from_json_string with instances """

        r1 = Rectangle(2, 4)
        r1_list = [r1.to_dictionary()]

        r1_base_json = Base.to_json_string(r1_list)
        output = Base.from_json_string(r1_base_json)
        self.assertTrue(type(output) is list)
        self.assertEqual(output, json.loads(r1_base_json))

        s1 = Square(4)
        s1_list = [s1.to_dictionary()]

        s1_base_json = Base.to_json_string(s1_list)
        output = Base.from_json_string(s1_base_json)
        self.assertTrue(type(output) is list)
        self.assertEqual(output, json.loads(s1_base_json))

    def test_base_from_json_string_more_args(self):
        """ test the from_json_string with more args than expected """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.from_json_string([r1.to_dictionary()], [s1.to_dictionary()])

    def test_base_from_json_string_no_args(self):
        """ test the from_json_string with no args """

        r1 = Rectangle(5, 4)
        s1 = Square(5)

        with self.assertRaises(TypeError):
            Base.to_json_string()
