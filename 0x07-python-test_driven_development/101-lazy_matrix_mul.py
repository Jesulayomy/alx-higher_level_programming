#!/usr/bin/python3
"""

    This module uses the numpy module to perform

    a matrix multiplication easily
    
    7. Lazy matrix multiplication

    Write a function that multiplies 2 matrices by using the module NumPy

"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """

        Lazy multiplication of two matrices using numpy

    """

    return (numpy.matmul(m_a, m_b))
