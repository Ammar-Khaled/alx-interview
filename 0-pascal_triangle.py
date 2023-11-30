"""Define a method that generates Pascal's Triangle."""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing
    the Pascal's triangle of n in time O(n).
    """
    pascal_triangle = []

    for i in range(n):
        row_value = str(11 ** i)
        row_digits = [int(digit) for digit in row_value]
        pascal_triangle.append(row_digits)

    return pascal_triangle
