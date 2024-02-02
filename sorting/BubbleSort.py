"""Bubblesort.

Bubble sort has time complexity O(n^2).
"""


def bubblesort(input: list) -> list:
    """Returns sorted array."""
    if len(input) < 1:
        return []

    finish_counter: int = 0

    while finish_counter < len(input) - 1:

        for currentIdx in range(len(input) - 1):
            # print(
            #     f"ITERATION: finish: {finish_counter}; currentIdx: {currentIdx}; {input}"
            # )

            if input[currentIdx] > input[currentIdx + 1]:
                # Python way
                input[currentIdx], input[currentIdx + 1] = (
                    input[currentIdx + 1],
                    input[currentIdx],
                )

                # Non-Python way: use temp value
                # temp_value = input[currentIdx]
                # input[currentIdx] = input[currentIdx + 1]
                # input[currentIdx + 1] = temp_value

                # If switch is required, start over tracking
                finish_counter = 0
            else:
                # If no need for switching, then keep track
                finish_counter += 1

        currentIdx += 1

    return input


def optimized_bubblesort(input: list) -> list:
    """Optimized version of BubbleSort."""
    if len(input) < 1:
        return []

    for outer in range(len(input)):
        for left in range(len(input) - outer - 1):
            print(f"ITERATION: outer: {outer}; left: {left}; {input}")
            if input[left] > input[left + 1]:
                input[left], input[left + 1] = input[left + 1], input[left]

    return input
