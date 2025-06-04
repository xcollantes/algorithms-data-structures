"""You are given an m x n integer matrix grid where each cell is either 0
(empty) or 1 (obstacle).
You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to
the lower right corner (m - 1, n - 1) given that you can eliminate at most k
obstacles. If it is not possible to find such walk return -1.
"""

from collections import deque


def quickest_path(grid: list[list[int]], k: int) -> int:
    ROWS: int = len(grid)
    COLS: int = len(grid[0])

    queue = deque([])
    # x, y, steps, k
    queue.append((0, 0, 0, k))

    # Stores x, y, k as a combination.
    # or instance, you could reach a cell (r, c):
    #   After having eliminated 2 obstacles (rk = k - 2).
    #   After having eliminated 1 obstacle (rk = k - 1).
    # A set would be faster with read of O(n).
    visited: list[tuple[int, int, int]] = list()

    while queue:
        # Popleft since BFS. Popright would work too for DFS.
        x, y, steps, k_remain = queue.popleft()
        print(f"R: {x} C: {y}")
        print(f"visited: {visited}")
        print(
            f"queue: (x:{x}, y:{y}, step:{steps}, k_remaining:{k_remain})",
            end="\n\n",
        )

        if x == ROWS - 1 and y == COLS - 1:
            return steps

        print("not done")
        for x_offset, y_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (
                0 <= x + x_offset
                and x + x_offset < ROWS
                and 0 <= y + y_offset
                and y + y_offset < COLS
                and (x + x_offset, y + y_offset, k_remain) not in visited
            ):
                if grid[x + x_offset][y + y_offset] == 1 and k_remain > 0:
                    visited.append((x + x_offset, y + y_offset, k_remain))
                    queue.append((x + x_offset, y + y_offset, steps + 1, k_remain - 1))

                elif grid[x + x_offset][y + y_offset] == 0:
                    visited.append((x + x_offset, y + y_offset, k_remain))
                    queue.append((x + x_offset, y + y_offset, steps + 1, k_remain))

    return -1


def p(grid) -> None:
    print("========")
    for r in grid:
        print(r)


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.BFS, Tags.MATRIX, Tags.GRAPH],
    difficulty=Difficulty.HARD,
)
