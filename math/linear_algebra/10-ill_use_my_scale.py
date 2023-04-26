#!/usr/bin/env python3
import numpy as np

def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray.

    Args:
    - matrix: numpy.ndarray, the input array

    Returns:
    - tuple of integers, the shape of the input array
    """
    shape = tuple(np.array(matrix.shape))
    return shape