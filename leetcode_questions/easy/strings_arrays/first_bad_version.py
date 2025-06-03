"""278. First Bad Version

Easy

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since
each version is developed based on the previous version, all the versions after
a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is
bad. Implement a function to find the first bad version. You should minimize the
number of calls to the API.


Example 1:

Input: n = 5, bad = 4
Output: 4

Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.


Example 2:

Input: n = 1, bad = 1
Output: 1


Constraints:
1 <= bad <= n <= 2^31 - 1
"""

from unittest.mock import patch


def first_bad_version(n: int) -> int:
    """"""
    l = 0
    r = n + 1

    while l < r:
        m = (l + r) // 2

        if isBadVersion(m):
            r = m
        else:
            l = m + 1

    return l


def isBadVersion(to_check: int):
    """Define in patch."""
    pass


def test_first_bad_version():
    """pytest first_bad_version.py"""
    _evaluate(first_bad_version, 5, 4)
    _evaluate(first_bad_version, 1, 1)


def _evaluate(fn, n, bad):
    with patch(f"{__name__}.isBadVersion") as mock_isBadVersion:

        def mock_implementation(version):
            return version >= bad

        mock_isBadVersion.side_effect = mock_implementation

        assert fn(n) == bad
