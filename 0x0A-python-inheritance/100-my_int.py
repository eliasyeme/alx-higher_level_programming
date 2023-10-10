#!/usr/bin/python3
"""The rebel int module"""


class MyInt(int):
    """Custom int class with inverted == and !="""
    def __eq__(self, value):
        """Overide eq from parent class to !="""
        return self.real != value

    def __ne__(self, value):
        """Overide ne from parent class to =="""
        return self.real == value
