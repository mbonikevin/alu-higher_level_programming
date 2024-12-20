#!/usr/bin/python3
"""7 base geometry"""


class BaseGeometry:
    """area method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
