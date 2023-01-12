#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    top = 0
    bottom = 0

    for item in my_list:
        top += item[0] * item[1]
        bottom += item[1]

    return top / bottom
