#!/usr/bin/python3
"""Append string to file"""


def append_write(filename="", text=""):
    """Append string to file as utf-8 encoding

    Args:
        filname (str): file to write to
        text (str): text to write

    Returns:
        Number of file written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
