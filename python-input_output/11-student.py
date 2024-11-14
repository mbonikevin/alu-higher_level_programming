#!/usr/bin/python3
"""defines the student class"""


class Student:
    """student class representation"""

    def __init__(self, first_name, last_name, age):
        """initializes student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns student attributes as dict"""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """updates student attributes from dict"""
        for k, v in json.items():
            setattr(self, k, v)
