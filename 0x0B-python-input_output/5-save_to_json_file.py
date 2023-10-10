#!/usr/bin/python3
"""Write json to file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file as json

    Args:
        my_obj (dict): Object to write to file
        filename (str): file to write to
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file, indent=2)
