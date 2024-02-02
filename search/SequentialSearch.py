"""Implementation of Sequential Search."""

from typing import List

def main():
  my_list = [4,3,5,5,-1,-4,0,3,54,-1,34]
  print(UnorderedSearch(my_list, 0))

def OrderedSearch(list: List[int], element: int) -> int:
  """Searched ordered list.

  list: Ordered list integers.
  element: The int to search the list.

  Returns: Position index if element in list.
  """
  pos = 0
  while pos < len(list):
    if list[pos] == element:
      return pos
    else:
      pos += 1


def UnorderedSearch(list: List[int], element: int) -> int:
  """Searches unordered list.

  list: Unordered list integers.
  element: The int to search the list.

  Returns: Position index if element in list.
  """
  pos = 0
  while pos < len(list):
    if list[pos] == element:
      return pos
    else:
      pos += 1


if __name__=='__main__':
  main()
