#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Geometry class"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator

        Args:
            name (str): Name of parameter.
            value (int): Parameter to validate.

        Raises:
            TypeError: If value is not integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize rectangle

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
