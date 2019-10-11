
from typing import List



def main():
  list = [5,8,2,3,1,9]
  
  print(f'LIST: {list}')
  print(f'SORT: {mergeSort(list)}')

  
def mergeSort(arr: List[int]) -> List[int]:
  print(f'MergeTop: {arr}')

  if len(arr) > 1:
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    posL = 0
    posR = 0
    r = 0

    while posL < len(left) and posR < len(right):
      if left[posL] < right[posR]:
        arr[r] = left[posL]
        posL += 1
      else:
        arr[r] = right[posR]
        posR += 1
  
      r += 1
        
    while posL < len(left):
      arr[r] = left[posL]
      r += 1
      posL += 1
  	  
    while posR < len(right):
      arr[r] = right[posR]
      r += 1
      posR += 1
  	  
    print(f'MERGING: {arr}')
  

if __name__ == '__main__':
  main()
