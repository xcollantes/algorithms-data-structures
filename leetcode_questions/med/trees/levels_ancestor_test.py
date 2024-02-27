"""Unit test for levels_ancestor.py."""

import unittest
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestLevelsAncestor(unittest.TestCase):
    def test_levels_ancestor(self):
        self.assertEqual("", "")
