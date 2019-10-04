"""QuickSort implementation using Lomuto partition"""

from typing import List


def main():
  list = [5,3,8,0,2,4,2,9,0]
  print(f'LIST: {list}')
  lomutoQuickSort(list)
  print(f'SORT: {list}')


def lomutoQuickSort(arr: List[int]) -> List[int]:
  lomutoQuickSortHelper(arr, 0, len(arr) - 1)


def lomutoQuickSortHelper(arr: List[int], first, last) -> List[int]:
  if first < last:

    split = lomutoPartition(arr, first, last)

    lomutoQuickSortHelper(arr, first, split - 1)
    lomutoQuickSortHelper(arr, split + 1, last)


def lomutoPartition(arr: List[int], first, last):
  pivot = arr[first]

  left = first + 1
  right = last

  done = False

  while not done:

    while left <= right and arr[left] <= pivot:
      left += 1

    while arr[left] >= pivot and right >= left:
      right -= 1

    if right < left:
      done = True
    else:
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp

  return right


if __name__ == '__main__':
  main()
