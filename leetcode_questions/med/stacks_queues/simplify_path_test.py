"""Unit test for simplify_path.py."""

import unittest
import logging

from leetcode_questions.med.simplify_path import path

logging.basicConfig(level=logging.INFO, format="%(message)s")


class TestSimplifyPath(unittest.TestCase):
    def test_simplify_path(self):
        self.assertEqual(path("/home/"), "/home")
        self.assertEqual(path("/../"), "/")
        self.assertEqual(path("/home//foo/"), "/home/foo")
