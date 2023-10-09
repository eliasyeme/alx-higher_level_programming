#!/usr/bin/python3
"""Square module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Initialize square

        Args:
            size (int): size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
