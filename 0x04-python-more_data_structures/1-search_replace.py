#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        return [i if i != search else replace for i in my_list]

    return my_list
