#!/usr/bin/env python3

""" a function thta calculates the summ of a random number"""

def summation_i_squared(n):
    """ summation_i_squared = calculate the squared of a summ """
    while not isinstance(n, int) or n < 1:
        return None
    return sum(i**2 for i in range(1, n+1)) 