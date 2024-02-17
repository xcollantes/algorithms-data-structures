"""QuickSort.

Using Lomuto partition where the pivot element is the last element of list.


Select a pivot element then perform swaps to get the lesser values before the
pivot and greater values after.

Time complexity: O(n log n) on average; O(n^2) worst case; Since the partition
is not guaranteed to be the median, the algorithm potentially could take n^2.
"""


def quicksort(array: list, lower: int, upper: int) -> list:
    """Quick sort.

    Args:
        array: Unsorted array.  lower: Lower bound of array.  upper: Upper bound
        or array.

    Returns:
        Sorted array.
    """
    if lower < upper:
        pivot: int = partition(array, lower, upper)
        quicksort(array, lower, pivot - 1)
        quicksort(array, pivot + 1, upper)

    return array


def partition(array: list, lower: int, upper: int) -> int:
    """Return pivot element of list."""

    pivot: any = array[upper]

    # Pointer for greater element
    greater_ptr = lower - 1
    for curr_idx in range(lower, upper):
        if array[curr_idx] <= pivot:
            greater_ptr += 1
            array[greater_ptr], array[curr_idx] = array[curr_idx], array[greater_ptr]

    array[greater_ptr + 1], array[upper] = array[upper], array[greater_ptr + 1]

    return greater_ptr + 1
