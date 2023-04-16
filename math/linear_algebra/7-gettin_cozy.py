#!/usr/bin/env python3
import numpy
""" a functin that concatenates two matrices and return only one """


def cat_matrices2D(mat1, mat2, axis=0):
    return (numpy.concatenate((mat1, mat2), axis=axis))
    