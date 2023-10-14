#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square

        Args:
            size (int): size of the square
            x (int): X coordinate of the square
            y (int): Y coordinate of the square
            id (int): id of the class

        Raises:
            TypeError: If Any of the inputs are not integer
            ValueError: If size is less or equal to 0
            ValueError: If x or y are less than 0
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set height and width to size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size,
        )
