"""Bubblesort.

Bubble sort has time complexity O(n^2).
"""


def bubblesort(input: list) -> list:
    """Returns sorted array."""
    if len(input) < 1:
        return []

    finish_counter: int = 0
    currentIdx: int = 0

    while finish_counter < len(input) - 1:
        print(f"ITERATION: finish: {finish_counter}; currentIdx: {currentIdx}; {input}")

        # Once you reach the end of the list, return to start
        if currentIdx >= len(input) - 1:
            currentIdx = 0
        else:
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
