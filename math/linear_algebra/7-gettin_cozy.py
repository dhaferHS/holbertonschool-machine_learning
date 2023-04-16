#!/usr/bin/env python3
"""Concatenates two matrices along a specific axis."""  
def cat_matrices2D(mat1, mat2, axis=0):
    

    """Concatenates two matrices along a specific axis.
    Arguments:
    mat1 -- a 2D matrix
    mat2 -- a 2D matrix
    axis -- an integer representing the axis along which to concatenate the matrices
    
    Returns:
    A new 2D matrix that is the result of concatenating mat1 and mat2 along the specified axis.
    """
    result = []
    for i in range(len(mat1)):
        return (result.append(mat1[i] + mat2[i]))

