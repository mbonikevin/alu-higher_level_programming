#!/usr/bin/python3
"""defines the student class"""


class Student:
    """student representation"""

    def __init__(self, first_name, last_name, age):
        """initializes student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns attributes as dict"""
        return self.__dict__
