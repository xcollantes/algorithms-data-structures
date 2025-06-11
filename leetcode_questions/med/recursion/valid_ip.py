"""93. Restore IP Addresses

Medium

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s. You are not allowed to reorder or
remove any digits in s. You may return the valid IP addresses in any order.


Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]


Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]


Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


Constraints:

1 <= s.length <= 20
s consists of digits only.
"""

"""
backtrack(idx=0, dots=0, cur_ip="")
String: "25525511135"
         ^
         idx=0

├── Try segment "2" (i=1)
│   backtrack(idx=1, dots=1, cur_ip="2.")
│   String: "25525511135"
│            ^
│            idx=1
│   ├── Try segment "5" (i=1)
│   │   backtrack(idx=2, dots=2, cur_ip="2.5.")
│   │   String: "25525511135"
│   │             ^
│   │             idx=2
│   │   ├── Try "5" → backtrack(idx=3, dots=3, cur_ip="2.5.5.")
│   │   ├── Try "52" → backtrack(idx=4, dots=3, cur_ip="2.5.52.")
│   │   └── Try "525" → backtrack(idx=5, dots=3, cur_ip="2.5.525.")
│   │
│   ├── Try segment "55" (i=2)
│   │   backtrack(idx=3, dots=2, cur_ip="2.55.")
│   └── Try segment "552" (i=3)
│       backtrack(idx=4, dots=2, cur_ip="2.552.")
│
├── Try segment "25" (i=2)
│   backtrack(idx=2, dots=1, cur_ip="25.")
│   String: "25525511135"
│             ^
│             idx=2
│   ├── Try segment "5" (i=1)
│   │   backtrack(idx=3, dots=2, cur_ip="25.5.")
│   │   ├── Try "2" → backtrack(idx=4, dots=3, cur_ip="25.5.2.")
│   │   ├── Try "25" → backtrack(idx=5, dots=3, cur_ip="25.5.25.")
│   │   └── Try "255" → backtrack(idx=6, dots=3, cur_ip="25.5.255.")
│   │
│   ├── Try segment "52" (i=2)
│   └── Try segment "525" (i=3)
│
└── Try segment "255" (i=3) ✓ LEADS TO SOLUTIONS
    backtrack(idx=3, dots=1, cur_ip="255.")
    String: "25525511135"
               ^
               idx=3
    ├── Try segment "2" (i=1)
    │   backtrack(idx=4, dots=2, cur_ip="255.2.")
    │   ├── Try "5" → backtrack(idx=5, dots=3, cur_ip="255.2.5.")
    │   ├── Try "55" → backtrack(idx=6, dots=3, cur_ip="255.2.55.")
    │   └── Try "552" → backtrack(idx=7, dots=3, cur_ip="255.2.552.")
    │
    ├── Try segment "25" (i=2)
    │   backtrack(idx=5, dots=2, cur_ip="255.25.")
    │   └── Try "5" → backtrack(idx=6, dots=3, cur_ip="255.25.5.")
    │       └── Try "11135" → TOO LONG, break
    │
    └── Try segment "255" (i=3) ✓ LEADS TO SOLUTIONS
        backtrack(idx=6, dots=2, cur_ip="255.255.")
        String: "25525511135"
                      ^
                      idx=6
        ├── Try segment "1" (i=1)
        │   backtrack(idx=7, dots=3, cur_ip="255.255.1.")
        │   ├── Try "1" → backtrack(idx=8, dots=4, cur_ip="255.255.1.1.")
        │   │   └── Try "135" → backtrack(idx=11, dots=4, cur_ip="255.255.1.1.135.")
        │   │       └── idx=11 == len(s), dots=4 ✓ INVALID (too many dots)
        │   ├── Try "11" → backtrack(idx=9, dots=4, cur_ip="255.255.1.11.")
        │   │   └── Try "35" → backtrack(idx=11, dots=4, cur_ip="255.255.1.11.35.")
        │   └── Try "113" → backtrack(idx=10, dots=4, cur_ip="255.255.1.113.")
        │
        ├── Try segment "11" (i=2) ✓ SOLUTION PATH
        │   backtrack(idx=8, dots=3, cur_ip="255.255.11.")
        │   └── Try "135" → backtrack(idx=11, dots=4, cur_ip="255.255.11.135.")
        │       └── idx=11 == len(s), dots=4 ✓ ADD "255.255.11.135"
        │
        └── Try segment "111" (i=3) ✓ SOLUTION PATH
            backtrack(idx=9, dots=3, cur_ip="255.255.111.")
            └── Try "35" → backtrack(idx=11, dots=4, cur_ip="255.255.111.35.")
                └── idx=11 == len(s), dots=4 ✓ ADD "255.255.111.35"
"""


def test_valid_ip():
    """pytest valid_ip.py"""
    assert valid_ip("25525511135") == ["255.255.11.135", "255.255.111.35"]
    assert valid_ip("0000121231231231313123131") == ["0.0.0.0"]
    # assert valid_ip("101023") == [
    #     "1.0.10.23",
    #     "1.0.102.3",
    #     "10.1.0.23",
    #     "10.10.2.3",
    #     "101.0.2.3",
    # ]
    # assert valid_ip("1111") == ["1.1.1.1"]
    # assert valid_ip("010010") == ["0.10.0.10", "0.100.1.0"]


def valid_ip(s: str) -> list[str]:
    """
    "25525511135"

    """

    def backtrack(idx, dots, cur_ip):
        print(f"idx {idx} dots {dots} cur_ip {cur_ip}")

        # The base case.
        # There's always a trailing dot even if valid and a fifth dot that
        # indicates invalid.
        if dots > 4:
            return

        # The base case where we used all dots and we've traversed the string.
        if dots == 4 and idx == len(s):
            res.append(cur_ip[:-1])  # Trim the trailing dot from last recursion.

        # For cur segment, try up to 3 combos.
        for i in range(1, 4):

            if idx + i > len(s):
                break

            cur = s[idx : idx + i]

            print(f"consider: {cur}")

            # validate contents.
            if cur.startswith("0") and len(cur) > 1 or i == 3 and int(cur) > 255:
                continue

            backtrack(idx + i, dots + 1, cur_ip + cur + ".")

            print()

        print()

    res = []

    backtrack(0, 0, "")

    return res
