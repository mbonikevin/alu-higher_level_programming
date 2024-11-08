#!/usr/bin/python3
"""checks if instance or subclass"""


def is_kind_of_class(obj, a_class):
    """returns True if instance or subclass"""
    return isinstance(obj, a_class)
