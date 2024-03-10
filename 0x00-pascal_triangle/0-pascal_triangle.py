#!/usr/bin/python3
"""Pascal's Triangle"""
"""Psuedo code"""
"""
create a list to store the outer list
iterate through the number of rows
create an inner list to store the values
iterate through the inner list
find the value of the combination of n and k
append the value to the inner list
append the inner list to the outer list
 return the outer list
"""


def pascal_triangle(numRows):
    """Pascal's Triangle"""
    if (numRows <= 0):
        return ([])
    outer_list = []
    for n in range(0, numRows):
        inside_list = []
        for k in range(0, n + 1):
            val = int(findComb(n, k))
            inside_list.append(val)
        outer_list.append(inside_list)
    return outer_list


def findFact(n):
    """Find the factorial of a number"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def findComb(n, k):
    """Find the combination of n and k"""
    return findFact(n) / (findFact(k) * findFact(n - k))
