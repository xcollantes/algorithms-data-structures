"""
Given a string text, you want to use the characters of text to form as many
instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of
instances that can be formed.
"""

import logging


def count_balloons(text: str) -> int:
    """Return count of instances of word 'balloons'."""
    word = dict({"b": 0, "a": 0, "l": 0, "o": 0, "n": 0})
    for letter in text:
        if letter in word:
            word[letter] = word[letter] + 1

    # There are 2 Ls and 2 Os so integer divide to get all letters on the same
    # level
    word["l"] = word["l"] // 2
    word["o"] = word["o"] // 2

    logging.info(word)

    # Return the minimum since that will be the lowest number of complete
    # letters to make the word
    return min(word.values())
