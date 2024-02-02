"""Binary Search"""
from typing import List

def main():
  x = [3,5,-1,70,45,-41,0,52,6,4,78,24,34,678,89]
  x.sort()

  print(BinarySearchIter(x, 1000))

  print('Binary Search Recursive')
  print(BinarySearchRec(x, 1000))


def BinarySearchRec(list: List[int], element: int) -> bool:
  first = 0
  last = len(list)
  #print(list)
  mid = (first + last) // 2

  #print('MID: ', list[mid], ' ', list)
  print('MID: ', mid, ' ', list)

  if len(list) == 0:
    return False
  if list[mid] == element:
    return True
  if list[mid] > element:
    return BinarySearchRec(list[first:mid - 1], element)
  if list[mid] < element:
    return BinarySearchRec(list[mid + 1:last], element)


def BinarySearchIter(list: List[int], element: int) -> bool:
  first = 0
  last = len(list)

  while first != last:
    print(list[first:last])

    mid = (first + last) // 2

    print('MID: ', list[mid])

    if list[mid] == element:
      return True
    elif list[mid] > element:
      last = mid - 1
    elif list[mid] < element:
      first = mid + 1


  return False


if __name__ == "__main__":
  main()
