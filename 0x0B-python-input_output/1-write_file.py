#!/usr/bin/python3
"""Write string to file"""


def write_file(filename="", text=""):
    """Write string to file as utf-8 encoding

    Args:
        filname (str): file to write to
        text (str): text to write
    """
    with open(filename, "w", encoding="UTF8") as file:
        return file.write(text)
