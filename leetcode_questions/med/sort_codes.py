"""Sort product codes based on a precedence.

Precedence is always the alphabet but in a different order.
"""

import logging
import string

logging.basicConfig(level=logging.INFO, format="%(message)s")


def custom_sort(code: str, precedence: str) -> str:
    """Map the code to a real alphabet for sorting."""
    ordered_alphabet: str = string.ascii_lowercase

    key: str = ""
    for letter in code:
        key += ordered_alphabet[precedence.index(letter)]

    logging.info("code: %s with key: %s", code, key)
    return key


def sort_productcodes(codes: list[str], precedence: str) -> list[str]:
    return sorted(codes, key=lambda c: custom_sort(c, precedence))


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.SORTING, Tags.STRING],
    difficulty=Difficulty.MEDIUM,
)
