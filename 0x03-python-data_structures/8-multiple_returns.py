#!/usr/bin/python3
def multiple_returns(sentence):
    c = None
    l = 0
    if sentence:
        c = sentence[0]
        l = len(sentence)
    return (l, c)
