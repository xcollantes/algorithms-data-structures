"""
Given a string s, return the longest palindromic substring in s.

"""

from collections import deque


def palindrome(s: str) -> str:
    """Return longest palindrome substring."""
    left = 0
    right = len(s) - 1

    current = ""
    while right > len(s) // 2:
        if s[left] == s[right]:
            logging.info(
                "new current: %s",
            )
            current = s[left:right]

        left += 1
        right -= 1

    return current


def is_palindrome(s: str) -> bool:
    q = deque(s)

    while len(q) > 1:
        left = q.popleft()
        right = q.pop()
        if left != right:
            return False

    return True
