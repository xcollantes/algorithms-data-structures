"""54. Spiral Matrix

Medium

Given an m x n matrix, return all elements of the matrix in spiral order.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

import unittest

from leetcode_questions.med.strings_arrays.spiral_matrix import spiral_matrix


class TestSpiralMatrix(unittest.TestCase):
    def test_spiral_matrix(self):

        # https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg
        self.assertEqual(
            spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        )

        # https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg
        self.assertEqual(
            spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        )
