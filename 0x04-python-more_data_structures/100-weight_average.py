#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        prd, sum = 0, 0
        for x, y in my_list:
            prd += x * y
            sum += y
        return prd / sum
    return 0
