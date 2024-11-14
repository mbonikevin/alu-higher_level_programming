#!/usr/bin/python3
"""1 write file"""


def write_file(filename="", text=""):
    """ function to write"""
    with open(filename, "w", encoding="utf-8") as me:
        num = me.write(text)
        return num
