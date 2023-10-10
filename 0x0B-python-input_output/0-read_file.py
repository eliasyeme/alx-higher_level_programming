#!/usr/bin/python3
"""Module to read file"""


def read_file(filename=""):
    """Read file as utf-8 encoding

    Args:
        filename (str): Name of the file to read from
    """
    with open(filename, "r", encoding="UTF8") as file:
        print(file.read(), end="")
