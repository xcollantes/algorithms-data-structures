"""67. Add Binary

Easy

Given two binary strings a and b, return their sum as a binary string.


Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


def test_add_binary():
    """pytest add_binary.py"""
    assert add_binary("11", "1") == "100"
    assert add_binary("1010", "1011") == "10101"
    assert add_binary("1111", "1111") == "11110"
    assert add_binary("1111", "0000") == "1111"


def add_binary(a: str, b: str) -> str:
    """"""
    # Find max length to continue operations.
    max_len = max(len(a), len(b))

    # make the strings equal length.
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""

    # The rule for adding binary is x + y = z where z is 1 if greater than 0.
    # Carry is the carry over if z is greater than 1.
    carry = 0

    for i in range(max_len - 1, -1, -1):
        print(f"i {i} {a[i]} {b[i]}")

        total = int(a[i]) + int(b[i]) + carry

        d = total % 2
        carry = total // 2

        result = str(d) + result

        print(f"    carry: {carry} d {d} result {result}")

    if carry:
        result = "1" + result

    return result


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STRING, Tags.MATH, Tags.BIT_MANIPULATION, Tags.BINARY],
    difficulty=Difficulty.EASY,
)
