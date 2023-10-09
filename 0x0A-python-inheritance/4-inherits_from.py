#!/usr/bin/python3
"""Check inheritance of a class"""


def inherits_from(obj, a_class):
    """Check inheritance from a class
    Args:
        obj (object): base object
        a_class (any): class to check
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
