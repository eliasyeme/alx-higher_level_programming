#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for i, c in enumerate(str):
        if i == n:
            continue
        else:
            s += c
    return s
