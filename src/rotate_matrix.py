"""Rotate a matrix by 90 degrees."""


def rotate_in_place(matrix):
    """
    Modify and return the original matrix.

    rotated 90 degrees clockwise in place.
    """
    try:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n//2):
            for j in range(i, m-1-i):
                ii, jj = i, j
                hold = matrix[ii][jj]
                for _ in range(3):
                    matrix[ii][jj] = matrix[n-1-jj][ii]
                    ii, jj = n-1-jj, ii
                matrix[ii][jj] = hold
    except IndexError:
        return matrix
    return matrix
