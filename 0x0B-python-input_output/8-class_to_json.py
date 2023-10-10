#!/usr/bin/python3
"""Dictionary discription"""


def class_to_json(obj):
    """Dictionary description

    Args:
        obj (any): Serializable class

    Return:
        dictionary description with simple
        data structure
    """
    return obj.__dict__
