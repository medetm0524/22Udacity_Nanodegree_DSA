# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 23:24:50 2022

@author: mmd20
"""



#%%

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    def binary_search_recursive(array, target, start_index, end_index):
        if start_index > end_index:
            return -1
    
        mid_index = (start_index + end_index) // 2
        mid_element = array[mid_index]
    
        if mid_element == target:
            return mid_index
    
        index_left_side = binary_search_recursive(array, target, start_index, mid_index - 1)
        index_right_side = binary_search_recursive(array, target, mid_index + 1, end_index)
    
        return max(index_left_side, index_right_side)

    start_index = 0
    end_index = len(input_list)-1    

    return binary_search_recursive(input_list, number, start_index, end_index)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


