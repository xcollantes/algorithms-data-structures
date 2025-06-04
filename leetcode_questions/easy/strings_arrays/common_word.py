"""819. Most Common Word

Given a string paragraph and a string array of the banned words banned, return
the most frequent word that is not banned. It is guaranteed there is at least
one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in
lowercase.
"""

import re


def most_common_word(paragraph: str, banned: list[str]) -> str:
    # Split and clean.
    words = re.findall("\w+", paragraph.lower())

    # Track counts.
    wc: dict[str, int] = {}

    # Iterate O(n).
    for word in words:
        # Filter out banned.
        if word not in banned:
            wc[word] = wc.get(word, 0) + 1

    # Return lowercase.
    return max(wc, key=lambda x: wc[x])
