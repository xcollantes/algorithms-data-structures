"""2696. Minimum String Length After Removing Substrings

Easy

You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce
new "AB" or "CD" substrings.

Example 1:

Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
Example 2:

Input: s = "ACBBD"
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.


Constraints:

1 <= s.length <= 100
s consists only of uppercase English letters.
"""


def minLength(s: str) -> int:
    """
    ABFCACDB
     i
    stack = [FC]
    """
    stack = []
    for i in range(len(s)):

        if stack:
            print(f"i: {i} stack: {stack}; compare: {stack[-1] + s[i]}")
            if stack[-1] + s[i] == "AB" or stack[-1] + s[i] == "CD":
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])

    return len(stack)


# pytest min_length_remove.py


def test_minLength_example_cases():
    # Test cases with AB and CD removals
    assert minLength("ABFCACDB") == 2
    assert minLength("ACBBD") == 5
    assert minLength("ABCD") == 0


def test_minLength_edge_cases():
    # Empty string
    assert minLength("") == 0
    # Single character
    assert minLength("A") == 1
    # No removable substrings
    assert minLength("XYZ") == 3


def test_minLength_mixed_cases():
    # Mixed removals with non-removable characters in between
    assert minLength("AXBYCZDX") == 8
    # Complex case with multiple removals
    assert minLength("ABCACDBABD") == 0
