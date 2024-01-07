#!/usr/bin/python3
"""Defines a matrix multiplication function using numPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.
    """

    return (np.matmul(m_a, m_b))
