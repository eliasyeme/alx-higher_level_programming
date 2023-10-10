#!/usr/bin/python3
"""Object to json"""
import json


def to_json_string(my_obj):
    """Json representation of an object

    Args:
        my_obj (dict): object to convert

    Returns:
        Json representation
    """
    return json.dumps(my_obj)
