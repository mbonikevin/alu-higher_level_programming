#!/usr/bin/python3
"""11 square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """special method"""
    def __init__(self, size):
        """seting size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area method"""
        return self.__size * self.__size

    def __str__(self):
        """__str__"""
        return "[Square] {}/{}".format(self.__size, self.__size)
