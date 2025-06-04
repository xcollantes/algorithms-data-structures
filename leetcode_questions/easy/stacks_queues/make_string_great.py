"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and
s[i + 1] where:

0 <= i <= s.length - 2 s[i] is a lower-case letter and s[i + 1] is the same
letter but in upper-case or vice-versa.  To make the string good, you can choose
two adjacent characters that make the string bad and remove them. You can keep
doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique
under the given constraints.

Notice that an empty string is also good.
"""


def make_great(s: str) -> str:
    """Return string with no bad characters."""

    stack = []

    for idx in range(len(s)):
        if stack and stack[-1] == s[idx].swapcase():
            stack.pop()
        else:
            stack.append(s[idx])

    return "".join(stack)


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STACK, Tags.STRING],
    difficulty=Difficulty.EASY,
)
