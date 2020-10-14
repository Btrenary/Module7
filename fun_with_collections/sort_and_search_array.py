"""
Author: Brady Trenary
Program: sort_and_search_array.py

"""
import array as arr

baseball_teams = arr.baseball_teams = ['Cubs', 'Cardinals', 'Pirates', 'Reds', 'Brewers']


def search_array(a):
    if a in baseball_teams:
        return baseball_teams.index(a)
    else:
        return '-1'


def sort_array():
    baseball_teams.sort()
    sorted_array = baseball_teams
    return sorted_array
    # used return to later be called in the main

if __name__ == '__main__':
    search_array('Pirates')
    sort_array()



