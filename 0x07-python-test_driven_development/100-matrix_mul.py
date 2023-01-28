#!/usr/bin/python3
"""

    This module solves task 6: Write a function that multiplies 2 matrices:

    using matrix multiplication method

"""


def matrix_mul(m_a, m_b):
    """

        MAtrix multiplication with appropriate errors

        for different cases listed

        m_a and m_b must be validated with these requirements in this order

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for lst in m_a:
        if not isinstance(lst, list):
            raise TypeError("m_a must be a list of lists")
    for lst in m_b:
        if not isinstance(lst, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == []:
        raise ValueError("m_a can't be empty")
    for lst in m_a:
        if lst == []:
            raise ValueError("m_a can't be empty")
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for lst in m_b:
        if lst == []:
            raise ValueError("m_b can't be empty")

    for lst in m_a:
        for elm in lst:
            if not type(elm) in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for lst in m_b:
        for elm in lst:
            if not type(elm) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    for lst in m_a:
        if len(lst) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for lst in m_b:
        if len(lst) != len(m_b[0]):
            raise TypeError("each row of m_a must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for rw in range(len(m_a)):
        lst = []
        for clm in range(len(m_b[0])):
            lst += [0]
        result += [lst]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
