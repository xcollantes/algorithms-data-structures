"""Unit test for sort_codes.py."""

import unittest

from leetcode_questions.sort_codes import sort_productcodes


class TestSortCodes(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(
            sort_productcodes(["dim", "wld", "sf", "sd"], "bpufvhsmkercowyltqxnjiadzg"),
            [
                "sf",
                "sd",
                "wld",
                "dim",
            ],
        )
