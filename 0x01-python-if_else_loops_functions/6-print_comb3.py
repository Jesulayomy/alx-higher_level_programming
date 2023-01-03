#!/usr/bin/python3
for tens in range(0, 10):
    for units in range(0, 10):
        if units > tens:
            if tens != 8:
                print("{0}{1}, ".format(tens, units), end="")
            else:
                print("{0}{1}".format(tens, units))
