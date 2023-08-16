#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    total_sum = 0
    for element in unique_list:
        total_sum += int(element)
    return total_sum
