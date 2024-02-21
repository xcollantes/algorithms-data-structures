"""Unit test for breadth_first_search.py."""

import unittest
import logging

from breadth_first_search.breadth_first_search import bfs


logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestBfs(unittest.TestCase):
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

    def test_bfs_recursive(self):
        answer = bfs(self.graph_hashmap, 0)
        logging.info(answer)
        self.assertEqual(answer, set([0, 1, 2, 3, 4]))
