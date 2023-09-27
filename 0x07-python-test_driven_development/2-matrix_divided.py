#!/usr/bin/python3
""" Matrix division module """


def matrix_divided(matrix, div):
    """Divide a matrix

    Args:
        matrix (list[list[float | int]]): list of lists of floats or ints
        div (int | float): divisor
    Raises:
        TypeError: If matrix is not list of lists of floats or ints
        TypeError: If each row of the matrix is not same size
        TypeError: If div is not a number (int or float)
        ZeroDivisionError: if div is zero
    Return:
        New matrix with the division result
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(el, int) or isinstance(el, float)for el in
        [n for row in matrix
            for n in row])):

        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
