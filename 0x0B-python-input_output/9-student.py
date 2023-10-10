#!/usr/bin/python3
"""Student module"""


class Student:
    """Represent student class"""
    def __init__(self, first_name, last_name, age) -> None:
        """Initialize student

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation

        Returns:
            Dictionary representaion of this class
        """
        return self.__dict__
