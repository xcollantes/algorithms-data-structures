"""Unit test for shortest_path_obstacles.py."""

import unittest
import logging

from leetcode_questions.hard.bfs.shortest_path_obstacles import quickest_path

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestShortestPathObstacles(unittest.TestCase):
    def test_shortest_path_obstacles(self):

        # The shortest path without eliminating any obstacle is 10. The shortest
        # path with one obstacle elimination at position (3,2) is 6. Such path
        # is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
        # https://assets.leetcode.com/uploads/2021/09/30/short1-grid.jpg
        #
        # https://docs.google.com/spreadsheets/d/11Ugiz7lpMj9YyUmsbkE9BWzQGxQnoYu0AWoZbOS6lYQ/edit?usp=sharing
        self.assertEqual(
            quickest_path(
                grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1
            ),
            6,
        )

        # We need to eliminate at least two obstacles to find such a walk.
        # https://assets.leetcode.com/uploads/2021/09/30/short2-grid.jpg
        self.assertEqual(
            quickest_path(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1),
            -1,
        )
