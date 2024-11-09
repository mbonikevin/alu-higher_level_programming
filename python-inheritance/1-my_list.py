#!/usr/bin/python3
"""1 my list"""


class MyList(list):
    """subclass of list with a method to print the sorted list"""

    def print_sorted(self):
        """printnig the list in ascending order"""
        print(sorted(self))
