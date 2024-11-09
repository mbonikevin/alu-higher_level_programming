#!/usr/bin/python3
"""rectangle class that inherits from basegeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """special method """
    def __init__(self, width, height):
        """seting with width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height


    def area(self):
        """area methos"""
        return self.__width * self.__height
