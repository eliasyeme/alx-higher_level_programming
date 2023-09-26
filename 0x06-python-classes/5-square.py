#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize the class

        Args:
            size (int, optional): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """getter for private property size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for private property size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square with # to stdout"""
        if (self.size):
            for _ in range(self.size):
                print("#" * self.size)
        else:
            print()
