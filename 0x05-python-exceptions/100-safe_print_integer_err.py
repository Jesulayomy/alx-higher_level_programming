#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except ValueError as er:
        stderr.write("Exception: {}\n".format(er))
        return False
    else:
        return True
