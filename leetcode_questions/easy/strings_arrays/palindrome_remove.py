"""680. Valid Palindrome II

Easy

Given a string s, return true if the s can be palindrome after deleting at most
one character from it.


Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.


Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


def valid_palindrome(s: str) -> bool:

    # Pointers on each side.
    left = 0
    right = len(s) - 1

    # As long as left and right are not passing.
    while left < right:
        print(f"l: {left}; r: {right}")

        # If same char, then palindrome is valid so far.
        if s[left] == s[right]:
            left += 1
            right -= 1

        # Different chars.
        else:
            print(
                f"s[left:right] {s[left:right]}; s[left:right][::-1] {s[left:right][::-1]}"
            )
            print(
                f"s[left + 1 : right + 1] {s[left + 1 : right + 1]}; s[left + 1 : right + 1][::-1] {s[left + 1 : right + 1][::-1]}"
            )

            return (
                s[left:right] == s[left:right][::-1]
                # Once encountering mismatch, check if one past the mismatch
                # will still yield a palindrome.
                or s[left + 1 : right + 1] == s[left + 1 : right + 1][::-1]
            )
    return True
