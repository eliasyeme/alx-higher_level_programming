#!/usr/bin/python3
"""Lookup attributes and methods of an object"""


def lookup(obj):
    """Lookup attributes and methods of an object

    Args:
        obj (object): object to lookup
    Return:
        list: list of objects
    """
    return dir(obj)
