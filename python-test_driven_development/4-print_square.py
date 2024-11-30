#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """print the results"""
    if not isinstance(size, int):
        raise TypeError("not an integer")
    if size < 0:
        raise ValueError("size is not >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
