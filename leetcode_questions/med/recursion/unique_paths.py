"""63. Unique Paths II

Medium

You are given an m x n integer array grid. There is a robot initially located at
the top-left corner (i.e., grid[0][0]). The robot tries to move to the
bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the
robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 *
109.


Example 1:

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2

Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


Example 2:

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1


Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""


def test_unique_paths():
    """pytest unique_paths.py"""
    assert unique_paths(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert unique_paths(obstacleGrid=[[0, 1], [0, 0]]) == 1
    assert unique_paths(obstacleGrid=[[0, 0]]) == 1


def unique_paths(obstacleGrid: list[list[int]]) -> int:

    def dfs(r, c) -> int:

        # OPTIMIZATION
        if (r, c) in memo:
            return memo[(r, c)]

        # Base case: reached the destination.
        if r == ROWS - 1 and c == COLS - 1:

            if obstacleGrid[r][c] == 0:
                return 1
            else:
                return 0

        # Check for out of bounds.
        if r >= ROWS or c >= COLS:
            return 0

        # Check for obstacle.
        if obstacleGrid[r][c] == 1:
            return 0

        # Calculate paths by going right and down only.
        paths = 0
        paths += dfs(r, c + 1)  # Move right.
        paths += dfs(r + 1, c)  # Move down.

        memo[(r, c)] = paths  # OPTIMIZATION
        return paths

    ROWS = len(obstacleGrid)
    COLS = len(obstacleGrid[0])

    memo = {}  # OPTIMIZATION

    # Always start from top-left corner.
    return dfs(0, 0)
