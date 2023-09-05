#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        c = ord(c)
        if c >= ord('a') and c <= ord('z'):
            c = c - (ord('a') - ord('A'))
        upper += chr(c)
    print(upper)
