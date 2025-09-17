"""168. Excel Sheet Column Title

Easy

Given an integer columnNumber, return its corresponding column title as it
appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:

Input: columnNumber = 1
Output: "A"


Example 2:

Input: columnNumber = 28
Output: "AB"


Example 3:

Input: columnNumber = 701
Output: "ZY"


Constraints:

1 <= columnNumber <= 231 - 1
"""

import string


def test_excel():
    """pytest excel.py"""
    assert excel(1) == "A"
    assert excel(28) == "AB"
    assert excel(701) == "ZY"


def excel(columnNumber: int) -> str:

    print(string.ascii_uppercase)

    alpha = string.ascii_uppercase
    a = 0

    cell = ""
    iters = columnNumber // 26

    for i in range(columnNumber):

        cell = alpha[i % 26]

        print(f"{alpha[:iters]}{cell} -> {i}")

    return f"{alpha[:iters]}{cell}"
