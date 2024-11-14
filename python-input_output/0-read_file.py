#!/usr/bin/python3
"""0 read file"""


def read_file(filename=""):
    """opening a file """
    with open(filename, encoding="utf-8") as a:
        print("{}".format(a.read()), end="")
