"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


def reverse_words(s: str) -> str:
    answer = []
    current_word = ""

    for c in s:
        if c != " ":
            current_word += c
        elif current_word != "":
            answer.append(current_word)
            current_word = ""

    if current_word != "":
        answer.append(current_word)

    return " ".join(answer[::-1])


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STRING],
    difficulty=Difficulty.MEDIUM,
)
