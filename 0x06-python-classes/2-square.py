#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize the class

        Args:
            size (int, optional): Size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
