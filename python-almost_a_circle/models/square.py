#!/usr/bin/python3
"""Defines a Square class, inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a subclass of Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
            x (int): The x coordinate of the square's position.
            y (int): The y coordinate of the square's position.
            id (int): The unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square, equivalent to width and height."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, updating both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square's attributes.

        Args:
            *args (ints): Positional arguments for updating attributes.
                - 1st argument: id
                - 2nd argument: size
                - 3rd argument: x
                - 4th argument: y
            **kwargs (dict): Key-value pairs for updating attributes.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg if arg is not None else self.id
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v if v is not None else self.id
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
