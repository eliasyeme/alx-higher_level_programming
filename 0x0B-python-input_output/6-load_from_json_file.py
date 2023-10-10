#!/usr/bin/python3
"""Load json from file"""
import json


def load_from_json_file(filename):
    """Load json to an object from a file

    Args:
        filename (str): file to write from

    Returns:
        An object read from file
    """
    with open(filename, "r") as file:
        return json.load(file)
