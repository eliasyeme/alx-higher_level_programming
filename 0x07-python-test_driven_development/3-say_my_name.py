#!/usr/bin/python3
""" Full name printer module """


def say_my_name(first_name, last_name=""):
    """Print first and last name

    Args:
        frist_name (str): first name
        last_name (str): last name
    Raises:
        TypeError: If first_name or last_name are not str
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
