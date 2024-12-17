"""1297. Maximum Number of Occurrences of a Substring

Given a string s, return the maximum number of occurrences of any substring
under the following rules:

The number of unique characters in the substring must be less than or equal to
maxLetters.
The substring size must be between minSize and maxSize inclusive.


Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and
maxSize).

Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.


Constraints:

1 <= s.length <= 105
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s consists of only lowercase English letters.
"""


def occurrences(s: str, max_letters: int, min_size: int, max_size: int) -> int:
    # max_size can be ignored since the segment MUST be at least a min_size. So
    # a larger string will always contain the smaller common segment.

    str_count = {}

    # End is the min limit for a segment.
    for i in range(len(s) - min_size + 1):
        print(f"i: {i}; s: {s}; min: {min_size};")

        #
        segment = s[i: i + min_size]

        print(f"    segment: {segment}")

        # Dedupe the segment since number of unique characters in the substring
        # must be less than or equal to maxLetters.
        if len(set(segment)) <= max_letters:

            print(f"    len(segment): {len(segment)} <= max_letters: {max_letters}; str_count: {str_count}")

            str_count[segment] = str_count.get(segment, 0) + 1

    return max(str_count.values(), default=0)