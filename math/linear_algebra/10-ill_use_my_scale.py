#!/usr/bin/env python3
def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray.

    Args:
    - matrix: numpy.ndarray, the input array

    Returns:
    - tuple of integers, the shape of the input array
    """
    shape = tuple(matrix.shape[i] for i in range(len(matrix.shape)))
    return shape
