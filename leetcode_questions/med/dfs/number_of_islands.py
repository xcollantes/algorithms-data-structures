"""200. Number of Islands

Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

import collections


def test_num_islands():
    """Test islands."""
    assert (
        num_islands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        num_islands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )


def num_islands(grid: list[list[str]]) -> int:

    def engulf_island(r, c):

        adj = collections.deque([(r, c)])

        while adj:

            x, y = adj.popleft()

            # Check if boundaries.
            # Check if 1.
            if 0 <= x < ROWS and 0 <= y < COLS and grid[x][y] == "1":

                print(f"x {x} y {y} adj {adj}")

                # Change found 1 to 0.
                # Critical because other top level for loop will iterate and might
                # see as 1 again.
                grid[x][y] = "0"

                # Look around.
                for xd, yd in [(0, 1), (1, 0), (0, -1), (-1, 0)]:

                    # Append adj.
                    adj.append((x + xd, y + yd))

    ROWS = len(grid)
    COLS = len(grid[0])

    islands = 0

    # Traverse every cell
    for r in range(ROWS):

        for c in range(COLS):

            # If 1 is found, add island.
            if grid[r][c] == "1":
                islands += 1
                engulf_island(r, c)

    return islands
