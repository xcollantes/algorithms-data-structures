"""Unit test for shortest_path_obstacles.py."""

import unittest
import logging

from leetcode_questions.hard.shortest_path_obstacles import quickest_path

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestShortestPathObstacles(unittest.TestCase):
    def test_shortest_path_obstacles(self):
        self.assertEqual(
            quickest_path(
                grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1
            ),
            6,
        )
        self.assertEqual(
            quickest_path(grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1),
            -1,
        )
