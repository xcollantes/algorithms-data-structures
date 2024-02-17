"""Insertion sort.

For each iteration of the element (step_idx), you are comparing the (step_idx)
to each value behind the (step_idx).

Time complexity O(n^2).  Space complexity O(1) since there is a key value held
outside of the array.

Simple yet inefficient sorting algorithm. Iterate through each element and if
the next element is smaller than the current element, switch with the current
element then pass element behind the current element. Check with each element
behind current element to see where the passed element belongs.
"""


def insertion(input: list) -> list:
    """Insertion sort."""
    if len(input) < 1:
        return []

    # Iterates over the array O(n)
    for step_idx in range(1, len(input)):

        temp_value: any = input[step_idx]

        # Start at second element since we'll include first element as part of
        # sorted array.
        prev_idx: any = step_idx - 1

        print(f"input: {input}; prev_idx: {prev_idx}; temp: {temp_value};")

        while temp_value < input[prev_idx] and prev_idx >= 0:
            input[prev_idx + 1] = input[prev_idx]

            # Move down the "sub array"
            prev_idx -= 1

        input[prev_idx + 1] = temp_value

    return input
