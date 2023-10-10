#!/usr/bin/python3
"""Module to add attribute to object"""


def add_attribute(obj, att, value):
    """Add attribute to an object if possible

    Args:
        obj (any): The object to add to
        att (str): Attribute to add
        value (any): Value for the attribute

    Raises:
        TypeError: If attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
