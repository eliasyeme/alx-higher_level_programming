#!/usr/bin/python3

def safe_print_integer(value):
    try:
        for val in value:
            print("{:d}".format(val))
        return True
    except:
        return False

