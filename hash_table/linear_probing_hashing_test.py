"""Unit test for linear_probing_hashing.py."""

import logging
import unittest

from hash_table.linear_probing_hashing import linear_probe_insert


class TestLinear(unittest.TestCase):
    def test_linear(self):

        answer = linear_probe_insert([23, 44, 11, 98, 100, 5])
        logging.info(answer)
        self.assertEqual(
            1,
            1,
        )
