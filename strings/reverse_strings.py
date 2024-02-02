"""String manipulations.

We're using `list[]` without `from typing import List` since
Python3.9 introduced type hints without imports.
"""

from collections import deque


def quick(sentence: str) -> list[str]:
    """Built-in function."""
    words = sentence.split(" ")
    words.reverse()  # `.reverse()` is in place; returns nothing
    return words


def reverse_words(sentence: str) -> list[str]:
    """Simplest way."""
    # For each word
    # push onto array
    words: list[str] = sentence.split(" ")

    result: list[str] = []
    idx: int = len(words) - 1
    while idx >= 0:
        result.append(words[idx])
        idx -= 1

    print(result)
    return result


def reverse_words_deque(sentence: str) -> list[str]:
    """Use deque library."""
    stack: deque = deque(sentence.split(" "))

    result: list[str] = []
    while len(stack) > 0:
        result.append(stack.pop())

    print(result)
    return result


def slicing(sentence: str) -> list[str]:
    """Use slicing of array.

    Slicing is [start: stop : step].
    """
    words = sentence.split(" ")
    return words[::-1]
