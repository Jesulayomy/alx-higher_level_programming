#!/usr/bin/python3
"""

    This module returns a matrix which is the result of dividing

    each elements of 'matrix' by 'div'

    1. Divide a matrix

    Write a function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """

        Divides each element in a matrix by div, and handles

        the necessary errors

        Matrix must be a list of lists of integers or floats
        Each row of the matrix must be of the same size
        Div must be a number (integer or float)
        Div can’t be equal to 0
        All elements of the matrix should be divided by div, rounded to 
        2 decimal places 

    """

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)
    if matrix != []:
        prev = len(matrix[0])
    else:
        raise TypeError(err)
    for member in matrix:
        if not isinstance(member, list):
            raise TypeError(err)
        if member == []:
            raise TypeError(err)
        if len(member) != prev:
            raise TypeError("Each row of the matrix must have the same size")
        for num in member:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(err)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for each_list in matrix:
        new_list = []
        for each_element in each_list:
            result = each_element / div
            result = int((result * 100) + 0.5) / 100.0
            new_list += [result]
        new_matrix += [new_list]
    return new_matrix
