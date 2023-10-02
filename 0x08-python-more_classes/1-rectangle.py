#!/usr/bin/python3
"""Module for Rectangle"""


class Rectangle:
    """Rectangle class

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width: int=0, height: int=0) -> None:
        """Initialize rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self) -> int:
        """Get width"""
        return self.__width

    @width.setter
    def width (self, value: int) -> None:
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value) -> None:
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
