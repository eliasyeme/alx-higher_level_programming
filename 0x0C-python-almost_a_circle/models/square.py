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

    def update(self, *args, **kwargs):
        """Update attributes"""
        for i in range(len(args)):
            val = args[i]
            if i == 0 and val != None:
                self.id = val
            elif i == 1:
                self.size = val
            elif i == 2:
                self.x = val
            elif i == 3:
                self.y = val

        if args:
            return

        for k, v in kwargs.items():
            if k == "id" and v != None:
                self.id = v
            elif k == "size":
                self.width = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v
