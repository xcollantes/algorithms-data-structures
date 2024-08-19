"""Unit test for shortest_path_obstacles.py."""

import unittest
import logging

from leetcode_questions.hard.shortest_path_obstacles import quickest_path

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestShortestPathObstacles(unittest.TestCase):
    def test_shortest_path_obstacles(self):

        # The shortest path without eliminating any obstacle is 10. The shortest
        # path with one obstacle elimination at position (3,2) is 6. Such path
        # is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
        self.assertEqual(
            quickest_path(
                grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1
            ),
            6,
        )

        # We need to eliminate at least two obstacles to find such a walk.
        self.assertEqual(
            quickest_path(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1),
            -1,
        )
