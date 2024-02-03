"""Insertion sort.

Time complexity O(n^2).
Space complexity O(1) since there is a key value held outside of the array.
"""


def insertion(input: list) -> list:
    """Insertion sort."""
    if len(input) < 1:
        return []

    # Iterates over the array O(n)
    for stepIdx in range(1, len(input)):

        temp_value: any = input[stepIdx]
        prevIdx: any = stepIdx - 1

        print(f"input: {input}; prevIdx: {prevIdx}; temp: {temp_value};")

        while temp_value < input[prevIdx] and prevIdx >= 0:
            input[prevIdx + 1] = input[prevIdx]
            prevIdx -= 1

        input[prevIdx + 1] = temp_value

    return input
