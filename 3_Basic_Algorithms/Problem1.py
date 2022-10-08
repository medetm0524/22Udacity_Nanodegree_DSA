# -*- coding: utf-8 -*-

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    number_list = list()
    for i in range(number+1):
        number_list.append(i)
        
    def find_sqrt(number_list, number):
        middle = len(number_list)//2
        mid_element = number_list[middle]
        sq_middle = mid_element*mid_element
        
        if sq_middle == number:
            return mid_element
        
        if len(number_list)==1:
            return number_list[0]
        
        elif sq_middle < number:
            return find_sqrt(number_list[middle:], number)
        
        else:
            return find_sqrt(number_list[:middle], number)
            
    return find_sqrt(number_list, number)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")