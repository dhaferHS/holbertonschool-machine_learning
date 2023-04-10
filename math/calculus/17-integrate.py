#!/usr/bin/env python3

""" function that alculates the integral of a polynomial """
def poly_integral(poly, C=0):
    if not isinstance(poly, list) or not all(isinstance(x, (int, float)) for x in poly) or not isinstance(C, int):
        return None  # poly or C is not valid
    integral = [C]
    for i, coef in enumerate(poly):
        if not isinstance(coef, int):
            coef = float(coef)
        power = i + 1
        term = coef / power if power > 0 else coef
        if term.is_integer():
            term = int(term)
        integral.append(term)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
