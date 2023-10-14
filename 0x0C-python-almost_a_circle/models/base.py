#!/usr/bin/python3
"""Base class module"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return string from list of dictionary

        Args:
            list_dictionaries (list[dict]): List of dictionary

        Returns:
            str: json string
        """
        if list_dictionaries is None or\
            len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        fn = "{}.json".format(cls.__name__)
        with open(fn, "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                dl = [x.to_dictionary() for x in list_objs]
                file.write(cls.to_json_string(dl))
