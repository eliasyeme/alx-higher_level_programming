#!/usr/bin/python3
"""Check instance of a class"""


def is_same_class(obj, a_class):
    """Check instance of an object
    Args:
        obj (object): base object
        a_class (any): class to check
    """
    return type(obj) is a_class
