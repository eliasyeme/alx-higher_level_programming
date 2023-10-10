#!/usr/bin/python3
"""Json string to an object"""
import json


def from_json_string(my_str):
    """json string to an object

    Args:
        my_str (str): json string to convert

    Returns:
        object representation
    """
    return json.loads(my_str)
