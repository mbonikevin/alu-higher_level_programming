#!/usr/bin/python3
"""8 rectangle"""


from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """soecial method"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
