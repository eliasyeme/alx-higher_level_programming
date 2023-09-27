#!/usr/bin/python3
""" Add module """


def add_integer(a, b=98):
    """Add two integers
    Args:
        a (int | float): first number
        b (int | float): second number
    Returns:
        addition of the a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
