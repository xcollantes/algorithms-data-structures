"""You are given an m x n integer matrix grid where each cell is either 0
(empty) or 1 (obstacle).
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to
the lower right corner (m - 1, n - 1) given that you can eliminate at most k
obstacles. If it is not possible to find such walk return -1.
"""


def quickest_path(grid: list[list[int]], k: int) -> int:
    for x in range(len(grid)):
        for y in range(grid[0]):
            


def p(grid) -> None:
    print("========")
    for r in grid:
        print(r)