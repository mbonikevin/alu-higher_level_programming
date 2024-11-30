#!/usr/bin/python3
"""adding 2 integers"""


def add_integer(a, b=98):
    """rerurning addition of a and b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a not an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b not an integer")
    return int(a) + int(b)
