#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for idx in range(0, x):
            n += 1
            print("{}".format(my_list[idx]), end="")
        print()
    except IndexError:
        print("", end="")
        n -= 1
    return n
