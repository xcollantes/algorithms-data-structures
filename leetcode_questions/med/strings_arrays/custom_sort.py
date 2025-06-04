"""791. Custom Sort String

Medium

You are given two strings order and s. All the characters of order are unique
and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order, then x
should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
"""


def custom_sort(order: list[str], s: str) -> str:

    # Iterate over input s.
    # Reorder using new key map.
    # Return string "ordered".
    return "".join(sorted(s, key=lambda x: _key(order, x)))


def _key(order: list[str], letter: str) -> str:
    """Generate a custom key to sort by."""

    if letter not in order:
        return 0

    return order.index(letter)


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.SORTING, Tags.STRING],
    difficulty=Difficulty.MEDIUM,
)
