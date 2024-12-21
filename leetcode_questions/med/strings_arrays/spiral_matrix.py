"""54. Spiral Matrix

Medium

Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    ROWS = len(matrix)
    COLS = len(matrix[0])
    TOTAL = ROWS * COLS

    result = []

    # At first I used x and y as pointers but easier to keep track of separate
    # pointers for each direction.

    top = 0
    bottom = ROWS - 1

    left = 0
    right = COLS - 1

    # While loop to only stop when stop case is reached.
    # Why I use non-pre-populated (DP-style) list. Because a list of `None` will
    # count for the `len()`.
    while len(result) < TOTAL:
        print(f"t: {top}; b: {bottom}; l: {left}; r: {right}")

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        # Move top down by one.
        top += 1

        print(f"A    t: {top}; b: {bottom}; l: {left}; r: {right}")

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        # Move right inwards by one.
        right -= 1

        print(f"B    t: {top}; b: {bottom}; l: {left}; r: {right}")

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

            print(f"C    t: {top}; b: {bottom}; l: {left}; r: {right}")

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

            print(f"D    t: {top}; b: {bottom}; l: {left}; r: {right}")

        print(f"RESULT: {result}")
        print()

    return result
