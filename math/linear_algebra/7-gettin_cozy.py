def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    
    Arguments:
    mat1 -- a 2D matrix
    mat2 -- a 2D matrix
    axis -- an integer representing the axis along which to concatenate the matrices
    
    Returns:
    A new 2D matrix that is the result of concatenating mat1 and mat2 along the specified axis.
    """
    if axis == 0:
        result = []
        for row in mat1:
            result.append(row)
        for row in mat2:
            result.append(row)
        return result
    elif axis == 1:
        result = []
        for i in range(len(mat1)):
            result.append(mat1[i] + mat2[i])
        return result
    else:
        raise ValueError("Axis must be either 0 or 1.")
