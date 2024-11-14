#!/usr/bin/python3
"""creates a function to append to file"""


def append_write(filename="", text=""):
    """appends content to file"""
    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
