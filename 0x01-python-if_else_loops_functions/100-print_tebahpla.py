#!/usr/bin/python3
def alpha_rev():
    for c in reversed(range(ord('a'), ord('z') + 1)):
        if c % 2 != 0:
            c = c - (ord('a') - ord('A'))
        print(f"{c:c}", end="")
