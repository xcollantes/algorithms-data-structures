"""Unit test for count_and_say.py.

38. Count and Say

Run-length encoding (RLE) is a string compression method that works by
replacing consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run).

For example, to compress the string "3322251" we
replace "33" with "23", replace "222" with "32", replace "5" with "15" and
replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say
sequence.

The confusing part is that you have to perform the RLE on the result of the
previous function call.
"""

import unittest

from leetcode_questions.med.strings_arrays.count_and_say import (
    countAndSay,
    countAndSayIterative,
)


class TestCountAndSay(unittest.TestCase):
    def test_count_and_say(self):
        self.cases(countAndSay)
        self.crazy_cases(countAndSay)

    def test_iterative(self):
        self.cases(countAndSayIterative)
        self.crazy_cases(countAndSayIterative)

    def cases(self, fn):
        # Explanation:
        #     countAndSay(1) = "1"
        #     countAndSay(2) = RLE of "1" = "11"
        #     countAndSay(3) = RLE of "11" = "21"
        #     countAndSay(4) = RLE of "21" = "1211"
        print("fn(4)")
        self.assertEqual(fn(4), "1211")
        print("fn(5)")
        self.assertEqual(fn(5), "111221")
        print("fn(8)")
        self.assertEqual(fn(8), "1113213211")

        # Explanation:
        # This is the base case.
        self.assertEqual(fn(1), "1")

    def crazy_cases(self, fn):
        self.assertEqual(fn(10), "13211311123113112211")
        self.assertEqual(
            fn(20),
            "11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211",
        )
