#!/usr/bin/python3
"""9 recvtangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """special method"""
    def __init__(self, width, height):
        """deting width and height."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    