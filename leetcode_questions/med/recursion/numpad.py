"""17. Letter Combinations of a Phone Number

Medium

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


def test_simple_numpad():
    """pytest numpad.py"""
    assert numpad("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


def test_complex_numpad():
    """pytest numpad.py"""
    assert numpad("") == []
    assert numpad("2") == ["a", "b", "c"]


def numpad(digits: str) -> int:

    if len(digits) == 0:
        return []

    numpad = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }


    def recursive(combo: str, rest_digits: str):

        # base case
        if len(rest_digits) == 0:
            res.append(combo)
            return

        print(f"cur {numpad[rest_digits[0]]}")

        # process first digit on string
        for l in numpad[rest_digits[0]]:
            print(f"    {combo + l}")

            recursive(combo + l, rest_digits[1:])


    res = []
    recursive("", digits)

    print(res)
    return res













