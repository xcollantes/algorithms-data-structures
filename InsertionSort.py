
import random

def main():

  A = [5,4,2,1,3,0]
  print(A)

  currIndex = 0

  while currIndex <= len(A) - 1:
    print(f'currIndex: {currIndex}')

    currVal = A[currIndex]
    if currVal < A[currIndex - 1]:
      A[currIndex] = A[currIndex - 1]
      A[currIndex - 1] = currVal


      sortIndex = currIndex
      sortVal = A[sortIndex]
      while sortIndex >= 0:
        if A[sortIndex - 1] > sortVal:
          A[sortIndex] = A[sortIndex - 1]
          A[sortIndex - 1] = sortVal

        sortIndex -= 1
        currVal = A[sortIndex]

    currIndex += 1

  print(A)









if __name__ == '__main__':
  main()
