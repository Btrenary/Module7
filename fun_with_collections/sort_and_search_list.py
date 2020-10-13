"""
Author: Brady Trenary
Program: sort_and_search_list.py

"""

car_make = ['Jeep', 'Chevrolet', 'Ford', 'Dodge', 'Nissan']


def search_list(a):
    if a in car_make:
        return car_make.index(a)
    else:
        return '-1'


def sort_list():
    car_make.sort()
    sorted_list = car_make
    return sorted_list


if __name__ == '__main__':
    search_list('Ford')
    sort_list()