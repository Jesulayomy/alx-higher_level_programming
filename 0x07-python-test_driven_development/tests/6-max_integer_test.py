#!/usr/bin/python3
"""
    Unittest for max_integer([..])

    it checks a list and returns the highest value in the list

"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """

       This is a unittest class for the task 6-max_integer

       it checks multiple possible testcases

    """


    def test_list(self):
        """
            Checks if the largest int in list1 is number
        """

        list1 = [-1, 3, 5, 7, 9 ,-12 ,35 ,13 ,46 ,68 ,24 ,-57 ,24, 35, 4, 53, 24]
        number = 68
        self.assertEqual(max_integer(list1), number)

    def test_empty_list(self):
        """
            Checks case for an empty list
        """

        self.assertEqual(max_integer([]), None)

    def test_string_in_list(self):
        """
            Checks case for a string in the list
        """
        with self.assertRaises(TypeError):
            max_integer([0, 1, '2'])

    def test_string_as_list(self):
        """
            Checks case for a string as list
        """

        self.assertEqual(max_integer('Hello'), 'o')

    def test_one_list(self):
        """
            Checks case for single element list
        """

        self.assertEqual(max_integer([74]), 74)

    def test_expando_list(self):
        """
            Checks for the largest int in the list
        """

        list1 = [-1, 3, 5, 7, 9 , -70,35 ,13 ,46 ,68 ,24 ,-57 ,24, 35, 4, 53, 24]
        self.assertEqual(max_integer([i ** 2 for i in list1]), 70 * 70)


if __name__ == '__main__':
    unittest.main()
