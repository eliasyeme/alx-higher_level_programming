#!/usr/bin/python3
"""Square module"""


def print_square(size):
    """Print square of #

    Args:
        size (int): Size length of the square
    Raises:
        TypeError: If size is not an int
        ValueError: If size is less than 0
        TypeError: If size is float and less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return

    for _ in range(size):
        print("#" * size)
