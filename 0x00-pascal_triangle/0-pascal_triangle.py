#!/usr/bin/python3
"""Define a method that generates Pascal's Triangle."""
from math import factorial


def pascal_triangle(n):
    """
    Return a pascal triangle of n.

    Return a list of lists of integers representing
    the Pascal's triangle of n in time O(n).
    """
    pascal_triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            # iCj = i!/((i-j)!*j!)
            row.append(factorial(i)//(factorial(j)*factorial(i-j)))
        pascal_triangle.append(row)

    return pascal_triangle
