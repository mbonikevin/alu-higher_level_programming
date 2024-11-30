#!/usr/bin/python3
"""unittests for the function def max_integer(list=[]):"""


def max_integer(list=[]):
    """print max integer if available"""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
