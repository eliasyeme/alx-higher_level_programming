#!/usr/bin/python3
"""Module for Rectangle"""


class Rectangle:

    number_of_instances = 0

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initialize rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
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

    def area(self) -> int:
        """Calculate area"""
        return self.width * self.height

    def perimeter(self) -> int:
        """Calculate perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self) -> str:
        """String representation"""
        rep = ""
        if self.width == 0 or self.height == 0:
            return rep
        for _ in range(self.height):
            rep += ("#" * self.width) + "\n"

        return rep[:-1]

    def __repr__(self) -> str:
        """String representation"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self) -> None:
        """Called when rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
