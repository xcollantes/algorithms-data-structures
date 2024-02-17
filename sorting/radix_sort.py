"""Radix sort.

Iterate over each value and sort by the place of the element.  Radix sort
s best when the number of digits are similar for each value.
Relies on Counting Sort to sort the place.

With Counting Sort, duplicate eys are inserted into new array in the same
array.  This is called a Stable algorithm.

Counting Sort s best when the range is small in the array in this case
it is 0 - 9. If the values are strings, the characters can be mapped to integers
to fit this model.

The term "Radix" refers to the base of the inputs.  In this case, the inputs
are base 10 since the range of possible values per place is between 0 - 9.

Process:
    1.  Iterate through each place in the list of integers and use zero as
        placeholders for shorter digits. Example: [1234, 123] -> [1234, 0123].
    2.  Use Counting Sort for each column to sort the elements.
    3.  Repeat until the elements are sorted.

Time complexity (with Counting Sort): O( d (n + b) )
    - With an array [25, 200, 150, 1, 5, 80, 18, 12] there are eight
      elements so n = 8.
    - The largest place is 3 such as 200 and 150 so  = 3.
    - Possibilities for the element is 0 - 9 since we're dealing with digits
      so b = 10.  This is what the "Radix" refers to.  
      The length of the radix is iterated since a list of occurrences is 
      created.  

Space complexity:
Not an in-place algorithm since extra space is required.

Sources:
    - https://www.youtube.com/watch?v=Uey0-GOMtT8
    - https://www.simplilearn.com/tutorials/data-structure-tutorial/radix-sort
"""
import logging
import math
from typing import List
from unicodedata import digit


logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    logging.info("Radix sort")

    input1: list(int) = [25, 200, 150, 1, 5, 80, 18, 12]
    input2: list(int) = [24, 11, 0, 34, 89, 11, 12, 88, 88, 88]
    input3: list(int) = [98377, 98229, 98552, 94043, 98103]
    input4: list(int) = []

    logging.info("Sorted: %s", sorted(input3))
    logging.info("Solution: %s", radix_sort(input3))

    assert radix_sort(input1) == sorted(input1)
    assert radix_sort(input2) == sorted(input2)
    assert radix_sort(input3) == sorted(input3)
    assert radix_sort(input4) == sorted(input4)


def radix_sort(unsorted: list) -> list:
    """Radix sort.

    Args:
        input (list): List to sort.

    Returns:
        list: Sorted list.
    """
    if unsorted == []:
        return []

    radix: int = 10
    max_value: int = max(unsorted)
    digits: int = int(math.floor(math.log(max_value, radix))) + 1

    # Iterate "column" first
    for place in range(1, digits + 1):
        logging.info("calling on %s place", place)
        unsorted = counting_sort(unsorted, place, radix)
    return unsorted


def counting_sort(unsorted: list, place: int, radix: int) -> List:
    """Underlying Counting Sort for Radix Sort.

    Args:
        unsorted (list): Iteration of Radix sort to sort by place.
    """
    logging.info("unsorted: %s", unsorted)

    sorted_list: list = [0] * len(unsorted)
    num_occur: list = [0] * radix

    # Iterate through a place for all values in list
    for element in unsorted:

        # Get the digit at the given place
        place_isolated = get_digit_in_place(element, place, radix)
        logging.debug("place: %s", place_isolated)

        # Count for each occurrence of a digit
        num_occur[place_isolated] += 1
        logging.debug("occur for element %s: %s", element, num_occur)

    # Add up the numbers in the previous index
    for num in range(1, len(num_occur)):
        num_occur[num] = num_occur[num] + num_occur[num - 1]

    logging.debug("num_occur: %s", num_occur)

    for original_idx in range(len(unsorted) - 1, -1, -1):
        logging.debug("original index: %s", original_idx)
        digit: int = get_digit_in_place(unsorted[original_idx], place, radix)

        num_occur_value: int = num_occur[digit]
        logging.debug("num_occur_value: %s", num_occur_value)

        sorted_list[num_occur_value - 1] = unsorted[original_idx]

        num_occur[digit] -= 1

    return sorted_list


def get_digit_in_place(number: int, place: int, radix: int = 10) -> int:
    """Extract the number found in a given place.

    Args:
        number: An integer.
        place: A place in a number counting from the right. 
        radix: Base number used for range of digits. 

    Returns:
        Isolated digit. 
    """
    return int(number % radix ** place / radix ** (place - 1))


if __name__ == "__main__":
    main()
