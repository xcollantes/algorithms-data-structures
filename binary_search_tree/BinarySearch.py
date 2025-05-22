"""Binary Search"""

from typing import List


def main():
    x = [3, 5, -1, 70, 45, -41, 0, 52, 6, 4, 78, 24, 34, 678, 89]
    x.sort()

    # These are actually wrong but keeping since I wrote them when I was
    # younger.
    #
    # assert BinarySearchIter(x, 1000) == False
    # assert BinarySearchIter(x, 678) == True

    # Wrong because can't handle if target element is first element.
    #
    # assert BinarySearchIter(x, -41) == True

    # print("Binary Search Recursive")
    # assert BinarySearchRec(x, 1000) == False
    # assert BinarySearchRec(x, 678) == True

    print("Simple binary search")
    assert simple_binary_search(x, 1000) == False
    assert simple_binary_search(x, 678) == True
    assert simple_binary_search(x, -41) == True


def simple_binary_search(array: List[int], element: int) -> bool:
    array.sort()  # Must be sorted for binary search to work.

    left = 0

    # Minus one to handle case where element does not exist on farthest right
    # in array.
    right = len(array) - 1

    while left <= right:
        # Until left pointer is equal to or less than right pointer to handle
        # case where element is in farthest left in array.

        mid = (left + right) // 2

        if array[mid] == element:
            return True

        if array[mid] > element:
            right = mid - 1
        elif array[mid] < element:
            left = mid + 1

    return False


def BinarySearchRec(list: List[int], element: int) -> bool:
    first = 0
    last = len(list)
    # print(list)
    mid = (first + last) // 2

    # print('MID: ', list[mid], ' ', list)
    print("MID: ", mid, " ", list)

    if len(list) == 0:
        return False
    if list[mid] == element:
        return True
    if list[mid] > element:
        return BinarySearchRec(list[first : mid - 1], element)
    if list[mid] < element:
        return BinarySearchRec(list[mid + 1 : last], element)


def BinarySearchIter(list: List[int], element: int) -> bool:
    first = 0
    last = len(list)

    while first != last:
        print(list[first:last])

        mid = (first + last) // 2

        print("MID: ", list[mid])

        if list[mid] == element:
            return True
        elif list[mid] > element:
            last = mid - 1
        elif list[mid] < element:
            first = mid + 1

    return False


if __name__ == "__main__":
    main()
