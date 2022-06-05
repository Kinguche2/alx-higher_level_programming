#!/usr/bin/python3
def element_at(my_list, idx):
    for x in range(len(my_list)):
        if idx == -idx:
            return None
        elif idx > x:
            return None
    else:
        print("{}".format(my_list[idx]))
