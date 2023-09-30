#!/usr/bin/python3
"""Square module"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to proccess.
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text\
        .replace('.', '.\n\n')\
        .replace('?', '?\n\n')\
        .replace(':', ':\n\n')\
        .split(" ")

    text = [c for c in text if c != ""]
    text = " ".join(text)
    print(text, end="")
