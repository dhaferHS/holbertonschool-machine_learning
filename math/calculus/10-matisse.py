#!/usr/bin/env python3

"""a fonction that calculates the poly derivation of the calculation"""


def poly_derivative(poly):
    """ a function that calculates the poly derivation of the calculation"""
    if not isinstance(poly, list) or not all(isinstance(x, (int, float)) for x in poly):
        return None  # poly is not valid
    if len(poly) <= 1:
        return [0]  # derivative is 0
    return [i * poly[i] for i in range(1, len(poly))]
