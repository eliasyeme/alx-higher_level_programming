#!/usr/bin/python3
"""Define inherited list from list class"""


class MyList(list):
    """Inherits from list class"""
    def print_sorted(self):
        """Sort list ascending"""
        print(sorted(self))
