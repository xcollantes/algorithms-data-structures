"""Insertion sort.

Time complexity O(n^2).
Space complexity O(1) since there is a key value held outside of the array.
"""


def insertion(input: list) -> list:
    """Insertion sort."""
    if len(input) < 1:
        return []

    for stepIdx in range(1, len(input)):
        temp_value: any = input[stepIdx]
        prevIdx: any = stepIdx - 1

        while temp_value < input[prevIdx] and prevIdx >= 0:
            input[prevIdx] = temp_value
            prevIdx -= 1

        input[stepIdx] = temp_value

    return input
