

def main():
  A = [3, 5, 1, 9, -1, 0, -1, 23, 12]

  print(f'REGULAR_ARR: {A}')
  n = len(A)

  for a in range(n):
    for b in range(n-a-1):
      if A[b] > A[b + 1]:
        A[b], A[b + 1] = A[b + 1], A[b]

  print(f'BUBBLE_SORT: {A}')

if __name__ == '__main__':
  main()
