#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(*my_list)
    except ValueError:
        print(end="\n")
