"""
Given a string paragraph and a string array of the banned words banned, return
the most frequent word that is not banned. It is guaranteed there is at least
one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in
lowercase.
"""

import re


def most_common_word(paragraph: str, banned: list[str]) -> str:
    words = re.split("\W+", paragraph)

    cleaned: list = []
    for word in words:
        w: str = word.lower().strip()

        if w not in banned and w != "":
            cleaned.append(w)

    return max(cleaned, key=cleaned.count)
