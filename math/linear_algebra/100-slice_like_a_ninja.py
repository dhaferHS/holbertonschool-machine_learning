#!/usr/bin/env python3
"""slice a matrics along a specific axes"""
import numpy as np


def np_slice(matrix, axes={}):
    """slice a matrics along a specific axes"""
    slices = [slice(None)] * matrix.ndim  # create a slice for each axis
    for axis, index in axes.items():
        if axis >= 0 and axis < matrix.ndim:  # check if axis is a valid index
            slices[axis] = slice(*index)  # update the slice for the specified axis
    return matrix[tuple(slices)]  # convert the list of slices to a tuple and slice the matrix
