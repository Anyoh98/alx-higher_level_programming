#!/usr/bin/python
def search_replace(my_list, search, replace):
    if not my_list:
        my_list = []
    the_function = lambda item: replace if item == search else item
    new_list = list(map(the_function, my_list))
    return new_list
