#!/usr/bin/python3
"""rectangle class that inherits from basegeometry"""


class BaseGeometry:
    """basegeometry class with integer_validator method"""
    def integer_validator(self, name, value):
        """validates the value as a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """rectangle class that inherits from basegeometry"""
    def __init__(self, width, height):
        """initializes the width and height, both are validated"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """returns the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
