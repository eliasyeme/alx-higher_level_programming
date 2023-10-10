#!/usr/bin/python3
"""Append string to file"""


def append_write(filename="", text=""):
    """Append string to file as utf-8 encoding

    Args:
        filname (str): file to write to
        text (str): text to write
    """
    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
