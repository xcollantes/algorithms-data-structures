"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.  Open brackets must
be closed in the correct order.  Every close bracket has a corresponding open
bracket of the same type.
"""

from collections import deque
import logging


def valid_parens(s: str) -> bool:
    """Return true if balanced."""
    parens = {
        "[": "]",
        "{": "}",
        "(": ")",
    }

    left_stack = deque()
    for e in s:
        if e in parens:
            logging.info("Adding to stack: %s", e)
            left_stack.append(e)

        if e in parens.values():
            if left_stack:
                logging.info("Popping stack: %s", e)

                if not parens[left_stack.pop()] == e:
                    return False

            else:
                # Case where no left parens exist
                logging.info("No contents in stack: %s", e)
                return False

    if left_stack:
        return False
    return True


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STACK, Tags.STRING],
    difficulty=Difficulty.MEDIUM,
)
