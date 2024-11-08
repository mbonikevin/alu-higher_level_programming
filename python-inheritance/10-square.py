#!/usr/bin/python3
"""class Square that inherits from Rectangle"""


from 9-rectangle import Rectangle

class Square(Rectangle):
    """special method"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    """area method"""
    def area(self):
        return self.__size * self.__size

    """__str__"""
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
