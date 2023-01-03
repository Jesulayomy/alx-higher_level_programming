#!/usr/bin/python3
ascii_value = 122
while ascii_value > 96:
    print("{:c}{:c}".format(ascii_value, ascii_value - 33), end="")
    ascii_value -= 2
