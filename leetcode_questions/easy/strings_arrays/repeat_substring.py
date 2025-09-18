"""459. Repeated Substring Pattern

Easy

Given a string s, check if it can be constructed by taking a substring of it and
appending multiple copies of the substring together.


Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.


Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""


def test_repeat_substring():
    """pytest repeat_substring.py"""
    assert repeat_substring("abab") == True
    assert repeat_substring("aba") == False
    assert repeat_substring("abcabcabcabc") == True


def repeat_substring(s: str) -> bool:
    """
    Solution is O(n) time.

    Optimal way is to check for the overlapping pattern of the string and check
    if the original string is in the overlapping pattern.

    The first and last character are removed because they would be the redundant
    characters in the overlapping pattern.
    """

    print(f"s {s}")

    combined = s + s

    print(f"(s + s) {combined}")
    print(f"index: {combined[1 : -1]}")

    return s in combined[1:-1]


"""
The key insight: Removing edges forces us to find the original string using only the "internal overlaps" created by concatenation.

Visual Example with "abab":

Original: "abab"
Doubled:  "abab" + "abab" = "abababab"
        │    │            │    │
        └────┼────────────┼────┘
                │  overlap   │
Remove edges:  "bababa"
                └─ "abab" ─┘  (found!)

Why this works for repeating patterns:

When you have a repeating pattern like "ab|ab", doubling it creates:
"ab|ab" + "ab|ab" = "ab|ab|ab|ab"

The middle section "ab|ab|ab" contains the full original pattern "ab|ab" because the repeating units align perfectly.

Why it fails for non-repeating patterns:

With "aba" (no internal repetition):
Original: "aba"
Doubled:  "aba" + "aba" = "abaaba"
Remove edges: "baab"

There's no way to reconstruct "aba" from "baab" because "aba" doesn't have internal repetition that would survive the edge removal.

The core principle:
- Repeating patterns have redundancy - their internal structure can recreate the whole string
- Non-repeating patterns lose essential information when edges are removed

The edge removal acts as a "filter" that only allows strings with internal repetitive structure to be reconstructable.
"""
