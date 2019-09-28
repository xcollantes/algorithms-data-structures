
from typing import List



def main():
  list = [3,7,2,9,23,43,0,3,8]
  
  print(f'LIST: {list}')
  print(f'SORT: {mergeSort(list)}')
  
  
def mergeSort(arr) -> List[int]:
  if len(arr) > 1:
    mid = len(arr) // 2
	
    left = arr[:mid]
    right = arr[mid:]
	
    mergeSort(left)
    mergeSort(right)

    posL = 0
    posR = 0
    result = []

  while posL < len(left) and posR < len(right):
    if left[posL] < right[posR]:
      result.append(left[posL])
      posL += 1
    else:
      result.append(right[posR])
      posR += 1
      
  while posL < left[posL]:
    result.append(left[posL])
    posL += 1
	  
  while posR < right[posR]:
    result.append(right[posR])
    posR += 1
	  
  return result


if __name__ == '__main__':
  main()
