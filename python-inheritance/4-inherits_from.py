#!/usr/bin/python3
"""checks if an object is an instance of a subclass"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a subclass of a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
