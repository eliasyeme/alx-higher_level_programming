#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base class to be based on

    Attributes:
        __nb_objects (int): Number of instances from base
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initialize square

        Args:
            id (int): id of the class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
