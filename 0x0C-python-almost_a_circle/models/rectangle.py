#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): X coordinate of the rectangle
            y (int): Y coordinate of the rectangle

        Raises:
            TypeError: If Any of the inputs are not integer
            ValueError: If width or height are less or equal to 0
            ValueError: If x or y are less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        self.__error_helper(value, "width")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        self.__error_helper(value, "height")
        self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x"""
        self.__error_helper(value, "x")
        self.__x = value

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y"""
        self.__error_helper(value, "y")
        self.__y = value

    @staticmethod
    def __error_helper(value, an):
        if type(value) != int:
            raise TypeError(
                "{} must be an integer".format(an)
            )

        if value <= 0:
            symbol = ">"
            if an == "x" or an == "y":
                if value == 0:
                    return
                symbol = ">="

            raise ValueError(
                "{} must be {} 0".format(an, symbol)
            )
