#!/usr/bin/python3
"""Geometry module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


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

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {:d}/{:d}".format(
            self.__class__.__name__,
            self.__width,
            self.__height
        )
