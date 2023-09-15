#!/usr/bin/python3
def roman_to_int(roman_string):
    rn = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    if roman_string or (type(roman_string) is str):
        num = len(roman_string) - 1
        int_num = rn[roman_string[num]]
        for i in range(num, 0, -1):
            if rn[roman_string[i-1]] >= rn[roman_string[i]]:
                int_num += rn[roman_string[i-1]]
            else:
                int_num -= rn[roman_string[i-1]]

        return int_num
    return 0
