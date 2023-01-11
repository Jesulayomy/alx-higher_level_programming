#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = list(set(my_list))
    result = 0
    for number in uniques:
        result += number
    return result
