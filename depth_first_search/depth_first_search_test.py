"""Unit test for depth_first_search.py."""

import unittest
import logging

from depth_first_search.depth_first_search import dfs_stack, recursive_dfs


logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestDfs(unittest.TestCase):
    def setUp(self):
        # Graph is undirected since e refers back to 1, 2, and 3.
        #
        #    0
        #  / | \
        # 1  2  3
        #  \ | /
        #    4
        self.graph: list[tuple[int, int]] = [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 4),
            (2, 4),
            (3, 4),
            (4, 1),
            (4, 2),
            (4, 3),
        ]
        self.graph_hashmap: dict[int, int] = {
            0: [1, 2, 3],
            1: [4],
            2: [4],
            3: [4],
            4: [1, 2, 3],
        }

    def test_dfs_recursive(self):
        visited = list()
        self.assertEqual(recursive_dfs(visited, self.graph_hashmap, 0), [0, 1, 4, 2, 3])

    def test_dfs_stack(self):
        self.assertEqual(dfs_stack(self.graph_hashmap, 0), [0, 3, 4, 2, 1])
