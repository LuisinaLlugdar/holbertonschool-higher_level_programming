#!/usr/bin/python3
def uniq_add(my_list=[]):
    total_sum = 0
    for i in set(my_list):
        total_sum += i
    return total_sum
