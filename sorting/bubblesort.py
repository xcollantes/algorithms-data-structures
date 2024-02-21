"""Bubblesort.

Time complexity O(n^2) since the first iteration for each element then if the
array is backwards to start, then each element might have to move by as many
elements. This is usually the worst of the Time Complexities.

Space complexity O(1) since there needs to be a temp value.

At the worst scenario, you have to make the switch
on each element in the array/list. Then that move will be made
for each array/list element. n for each element then that can
happen n times so n * n or n^2.

Example: https://stackabuse.com/bubble-sort-in-python/
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


def swap_bubblesort(input: List[int]) -> List[int]:
    """Improved performance on Bubble Sort algorithm.

    Improvements:
    1)  NO-SWAP
        When no swap is made, that means list is already sorted.
        Algorithm is the same but will stop once the list is
        sorted.

    2)  IGNORE-ALREADY-SORTED
        We know Bubble Sort ends each pass with the largest number at
        the end of the list. The first pass guarantees that the last
        element or n is the largest element, then in the second pass
        the second to last element is the second-largest or n - 1, and
        so forth.

        This means for each pass, we can ignore one less element on the
        end of the list. More precisely, the k-th iteration, we only need
        to look at n - k + 1 number of elements.
    """
    if len(input) < 1:
        return input

    swapped: bool = True  # NO-SWAP
    num_of_iterations: int = 0  # IGNORE-ALREADY-SORTED
    idx: int = 0

    while swapped:  # NO-SWAP: Instead check for if a swap occurred
        swapped = False  # NO-SWAP

        # IGNORE-ALREADY-SORTED: Reduce the number elements to iterate
        # for each pass since we know the largest values "Bubble up" to
        # the end.
        while idx < len(input) - num_of_iterations - 1:

            # NO-SWAP: If this never occurs on a single pass, then you
            # can safely say the list is sorted without continuing
            # to the already sorted parts of the list.
            if input[idx] > input[idx + 1]:
                input[idx], input[idx + 1] = input[idx + 1], input[idx]

                swapped = True  # NO-SWAP

            idx += 1
        idx = 0
        num_of_iterations += 1  # IGNORE-ALREADY-SORTED: Add one for each pass

    return input
