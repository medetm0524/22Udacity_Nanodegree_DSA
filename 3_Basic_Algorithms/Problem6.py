# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:22:34 2022

@author: mmd20
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_val = ints[0]
    min_val = ints[0]
    
    for element in ints:
        if max_val < element:
            max_val = element
        
        if min_val > element:
            min_val= element

    print(min_val, max_val)
    return min_val, max_val
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")