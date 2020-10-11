"""
Author: Brady Trenary
Program: basic_list.py

"""


def make_list():
    u_list = []
    for i in range(0, 3):
        u_input = int(get_input())
        u_list.insert(i, u_input)
    return u_list

def get_input():
    pass
