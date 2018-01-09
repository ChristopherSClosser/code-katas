"""Modify and return the original matrix rotated 90 degrees clockwise in place."""


def rotate_in_place(matrix):
    """Rotate a matrix by 90 degrees."""
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
    except:
        return matrix
    return matrix


# def test_3_by_3():
#     """Test rotation of a 3x3 matrix."""
#     from rotate_matrix import rotate_matrix
#     matrix_input = [
#                         [1, 2, 3],
#                         [4, 5, 6],
#                         [7, 8, 9]
#                     ]
#
#     matrix_output = [
#                         [7, 4, 1],
#                         [8, 5, 2],
#                         [9, 6, 3]
#                     ]
#     assert rotate_matrix(matrix_input) == matrix_output
