#!/usr/bin/python3
"""9 rectangle"""


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """soecial method"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """area method"""
    def area(self):
        return self.__width * self.__height

    """__str__"""
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
