def uppercase(str):
    n = 0
    for char in str:
        ascii_value = ord(char)
        if ascii_value > 96 and ascii_value < 123:
            ascii_value -= 32
        print('{:c}'.format(ascii_value), end="")
    print()
