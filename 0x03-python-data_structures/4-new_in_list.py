#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.new()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.new()
    else:
        copy[idx] = element
        return new
