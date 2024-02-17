"""Selection sort.

Simple but still inefficient algorithm for sorting.  Iterate through 
the list to find the smallest value.  Then switch the position of the newly 
found smallest value with the front of the list.  

Process: 
    1. Iterate through the whole list to find the smallest value. 
    2. Assign the smallest value to a variable. 
    3. Replace the smallest value and the first value of the list. 
    4. Now you have the first element in the correct sort order.  Repeat. 

Time complexity: O(n^2).  Not good for large datasets. 
"""

import logging
from typing import Any

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    logging.info("Selection sort")

    input1: list(int) = [25, 20, 15, 1, 5, 8, 18, 12]
    input2: list(int) = [24, 11, 0, 34, 89, 11, 12, 88, 88, 88]
    input3: list(int) = []

    assert selection_sort(input1) == sorted(input1)
    assert selection_sort(input2) == sorted(input2)
    assert selection_sort(input3) == sorted(input3)


def selection_sort(unsorted: list) -> list:
    """Selection sort.

    Args:
        unsorted: List of elements to sort.

    Returns:
        Sorted list.
    """
    for a_idx in range(len(unsorted)):
        min_idx: int = a_idx

        # b_idx will reset after last comparison
        # Start b_idx after all the sorted values
        for b_idx in range(len(unsorted) - a_idx):
            if unsorted[min_idx] > unsorted[b_idx]:
                min_idx = b_idx

        # Exchange the values of smallest value found with first unsorted value
        unsorted[a_idx] = unsorted[min_idx]
        unsorted[min_idx] = unsorted[a_idx]

        # Other way to express exchange in Python
        # unsorted[a_idx], unsorted[min_idx] = unsorted[min_idx], unsorted[a_idx]

    return unsorted


if __name__ == "__main__":
    main()
