"""Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same. 

Return any possible rearrangement of s or return "" if not possible.

https://leetcode.com/problems/reorganize-string/description
"""


def reorganize_string(s: str) -> str:
    freq = {}

    # Iterate through each character.
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Sort characters by key descending.
    sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    print(f"Freq reverse sorted: {sorted_chars}")

    # Determines if possible to rearrange the string.
    # If the largest count in the sorted characters is greater than the length
    # divided by 2, then it's possible.
    #
    # The maxed out case would be "babcbcbc" where "b" would be half of the
    # total strings.
    if freq[sorted_chars[0]] > (len(s) + 1) // 2:
        return ""

    # Dynamic Programming array.
    result = [None] * len(s)

    i = 0
    for char in sorted_chars:
        print(f"char: {char}")

        # Alternates between i and i + 2 to construct the result.
        # Conceptually like using modular to choose from possible characters.
        for _ in range(freq[char]):
            # How does the count of each character get tracked?
            # This loop will loop for the count of each character.
            print(f"    i: {i}")

            if i >= len(s):  # Once i exceeds length, then reset to beginning.
                i = 1

            result[i] = char

            i += 2

    return "".join(result)
