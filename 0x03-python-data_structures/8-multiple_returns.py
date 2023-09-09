#!/usr/bin/python3
def multiple_returns(sentence):
    chr= None
    length = 0
    if sentence:
        chr = sentence[0]
        length = len(sentence)
    return (length, chr)
