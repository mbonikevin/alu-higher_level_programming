#!/usr/bin/python3
"""2 is same class"""


def is_same_class(obj, a_class):
    """returning true if obj is exactly an instance of a_class"""
    return type(obj) is a_class
