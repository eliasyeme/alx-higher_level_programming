#!/usr/bin/python3
def no_c(my_string):
    replaced = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            replaced += c
    return replaced
