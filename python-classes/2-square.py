#!/usr/bin/python3
"""this module defins a squar clas"""


class Square:
    """defines a squar with validashun for size""" 
    
    def __init__(self, size=0):
        """initializes the size of the squar""" 
        self.size = size

    @property
    def size(self):
        """getter for size""" 
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size with validashun""" 
        if type(value) is not int:
            raise TypeError("size must be an intiger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
