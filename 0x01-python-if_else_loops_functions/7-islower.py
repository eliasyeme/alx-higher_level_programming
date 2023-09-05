#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c >= ord('a') and c <= ord('z'):
        return True
    else:
        return False
