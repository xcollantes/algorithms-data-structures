"""Selection Sort"""

from typing import List



def main():
  A = [3,1,9,0,3,1,2]
  print(f'{A} of length {len(A)}')
  print(SelectionSort(A))


def SelectionSort(arr: List[int]) -> List[int]:
  minIndex = 0

  for e in range(len(arr)):
    for x in range(e + 1, len(arr)):
      print(f'starting at pos: {x}')
      if arr[minIndex] > arr[x]:
        minIndex = x

    print(f'For index:{e} found min at index: {arr[minIndex]}')

    arr[e], arr[minIndex] = arr[minIndex], arr[e]
    print(f'{arr} of length: {len(arr)}\n')
  return arr

if __name__=='__main__':
  main()
