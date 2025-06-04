"""670. Maximum Swap

Medium

You are given an integer num. You can swap two digits at most once to get the
maximum valued number.

Return the maximum valued number you can get.


Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.


Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.


Constraints: 0 <= num <= 108
"""


def max_swap(num: int) -> int:
    pos = list(str(num))
    print(pos)

    # Create a dict of the last of each digit to easily compare later.
    #
    # This takes care of duplicated digits since only the last index is
    # recorded.
    # {digit: last position index}
    last_pos = {}
    for i, d in enumerate(pos):
        last_pos[int(d)] = i

    print(last_pos)

    # Iterate over the numbers again with an index.
    for i, dig in enumerate(pos):
        print(f"i: {i}; dig: {dig};")

        # From the largest digit (9) look for digit in last digit dict.
        for d in range(9, int(d), -1):
            print(f"d: {d};")

            # If we find a digit in our dict which is larger, then replace.
            # We return right away since we only have one swap.
            last_index = last_pos.get(d, -1)
            if last_index > i:
                pos[i], pos[last_pos[d]] = pos[last_pos[d]], pos[i]
                return int("".join(pos))

    # Return num if no swaps have taken place.
    return num


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.STRING],
    difficulty=Difficulty.MEDIUM,
)
