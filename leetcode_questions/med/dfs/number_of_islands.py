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

import pytest


def test_num_islands():
    """pytest test_num_islands.py."""

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

    # assert (
    #     num_islands(
    #         [
    #             ["1", "1", "0", "0", "0"],
    #             ["1", "1", "0", "0", "0"],
    #             ["0", "0", "1", "0", "0"],
    #             ["0", "0", "0", "1", "1"],
    #         ]
    #     )
    #     == 3
    # )

    # assert (
    #     num_islands(
    #         [
    #             ["0", "0", "0", "1", "1"],
    #             ["0", "0", "0", "1", "1"],
    #             ["1", "0", "0", "1", "1"],
    #             ["0", "0", "0", "1", "1"],
    #         ]
    #     )
    #     == 2
    # )


def p(g):
    for i in g:
        print(i)


def num_islands(grid: list[list[str]]) -> int:

    def find_size(x, y):

        # initiate as stack with single first value to start reading stack
        stack = [(x, y)]

        while stack:

            a, b = stack.pop(0)

            print(f"POPPING a {a} b {b} from {stack}")

            # in bounds
            if 0 <= a < ROWS and 0 <= b < COLS and grid[a][b] == "1":

                # critical to mark as 0 to avoid other iterations from reading
                # as island
                grid[a][b] = "0"

                # look around
                for xo, yo in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                    print(f"appending {(a + xo, b + yo)}")

                    stack.append((a + xo, b + yo))


    ROWS = len(grid)
    COLS = len(grid[0])

    res = 0

    for r in range(ROWS):
        for c in range(COLS):

            # print(f"r {r} c {c}")
            if grid[r][c] == "1":
                res += 1
                find_size(r, c)

    print(f"result {res}")
    return res
