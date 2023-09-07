#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    def calc(a, b, op):
        if op == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    ops = "+-*/"
    op = argv[2]
    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    calc(int(argv[1]), int(argv[3]), op)
