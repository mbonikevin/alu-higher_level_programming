#!/usr/bin/python3
"""7 base geometry"""


class BaseGeometry:
    """area method"""
    def area(self):
        raise Exception("area() is not implemented")

    """integer_validator method"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
