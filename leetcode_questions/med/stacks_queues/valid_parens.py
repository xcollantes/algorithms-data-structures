"""20. Valid Parentheses

Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.  Open brackets must
be closed in the correct order.  Every close bracket has a corresponding open
bracket of the same type.

Example 1: Input: s = "()" Output: true

Example 2: Input: s = "()[]{}" Output: true

Example 3: Input: s = "(]" Output: false

Example 4: Input: s = "([])" Output: true
"""

from collections import deque


def is_valid(s: str) -> bool:
    # Track.
    parens = {"(": ")", "{": "}", "[": "]"}
    left_stack = deque()

    # Iterate by O(n).
    for e in s:
        print(f"E: {e}")

        if e in parens:
            print(f"APPENDING LEFT: {e}")
            left_stack.append(e)

        elif e in parens.values():
            print(f"RIGHT FOUND: {e}")

            if len(left_stack) <= 0:
                print("left_stack is empty, mismatched right paren.")
                return False

            left_pop = left_stack.pop()
            if parens[left_pop] != e:
                print(f"matching {parens[left_pop]} with {e}: mismatched; wrong order.")
                return False

    # Check stack AND s if empty.
    # If empty -> True; if contents -> False.
    if len(left_stack) <= 0:
        return True

    return False


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STACK, Tags.STRING],
    difficulty=Difficulty.MEDIUM,
)
