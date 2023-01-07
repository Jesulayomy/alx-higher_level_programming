#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    new_list = []
    index = 0
    for element in my_list:
        if index != idx:
            new_list += [element]
        index += 1
    my_list = new_list
    return my_list
