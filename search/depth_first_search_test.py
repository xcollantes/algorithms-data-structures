"""Unit test for depth_first_search.py."""

import unittest

from search.depth_first_search import dfs


class TestDfs(unittest.TestCase):
    def test_dfs(self):
        self.assertEquals(dfs())
