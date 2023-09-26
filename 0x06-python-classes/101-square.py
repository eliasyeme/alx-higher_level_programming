#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class

        Args:
            size (int, optional): Size of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter for private property position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square with # to stdout"""
        if (self.size):
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()

    def __str__(self):
        """Make square printable"""
        tmp = []
        if (self.size):
            for _ in range(self.position[1]):
                tmp.append("")
            for _ in range(self.size):
                tmp.append(" " * self.position[0] + "#" * self.size)
            return "\n".join(tmp)
        else:
            return ""
