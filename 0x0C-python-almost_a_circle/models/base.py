#!/usr/bin/python3
"""Base class module"""
import json
import os


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Create list from json string

        Args:
            json_string (str): json string

        Returns:
            list: list from json string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write list of object to file as json

        Args:
            list_objs (list[dict]): List of dictionary
        """
        fn = "{}.json".format(cls.__name__)
        with open(fn, "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                dl = [x.to_dictionary() for x in list_objs]
                file.write(cls.to_json_string(dl))

    @classmethod
    def create(cls, **dictionary):
        """Create instance with all attributes set

        Args:
            dictionary (dict): attributes to be set

        Returns:
            instance: new instance set with dictionary
        """
        if dictionary and len(dictionary):
            new = cls(1) if cls.__name__ == "Square" else cls(1, 1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Load instance from file"""
        fn = "{}.json".format(cls.__name__)
        if os.path.exists(fn):
            with open(fn, "r") as file:
                lst = cls.from_json_string(file.read())
                return [cls.create(**x) for x in lst]
        else:
            return []
