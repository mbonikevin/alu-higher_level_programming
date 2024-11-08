#!/usr/bin/python3
"""Module that defines a subclass of list with a method to print the list sorted."""


class MyList(list):
    """A subclass of list that includes a method to print the list in ascending order."""
    
    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))

    def __str__(self):
        """Return the string representation of the list."""
        return str(self)
