"""48. Rotate Image

Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

from re import T


def test_rotate_matrix():
    """pytest rotate_matrix.py"""
    # Test case 1: 3x3 matrix from Example 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_matrix(matrix1)
    assert matrix1 == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    # Test case 2: 4x4 matrix from Example 2
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    rotate_matrix(matrix2)
    assert matrix2 == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ]

    # Test case 3: 1x1 matrix (edge case)
    matrix3 = [[1]]
    rotate_matrix(matrix3)
    assert matrix3 == [[1]]

    # Test case 4: 2x2 matrix
    matrix4 = [[1, 2], [3, 4]]
    rotate_matrix(matrix4)
    assert matrix4 == [[3, 1], [4, 2]]

    # Test case 5: 5x5 matrix
    matrix5 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    rotate_matrix(matrix5)
    expected5 = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]
    assert matrix5 == expected5

    print("All test cases passed!")


def p(m):
    for r in m:
        print(r)


def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:

    # Depending on the way we rotate, the order of Reverse and then transpose is
    # important.

    # If you transpose then Reverse the cols instead of rows: 90 degree
    # counterclockwise rotation.

    # Reverse matrix.
    t = 0
    b = len(matrix) - 1
    while t < b:
        matrix[t], matrix[b] = matrix[b], matrix[t]
        t += 1
        b -= 1

    p(matrix)

    # transpose matrix.
    for x in range(len(matrix)):
        for y in range(x):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    p(matrix)
