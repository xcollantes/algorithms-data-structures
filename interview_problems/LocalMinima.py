


def main():
  A = [5,1,4,0]
  print(f'RESULT: {minima(A)}')

def minima(A):
  result = []

  if len(A) <= 1:
    return 0

  pos = 0
  n = pos + 1
  prev = 0
  while pos < len(A):
    if A[prev] >= A[pos] <= A[n]:
      result.append(pos)
    pos += 1
    prev = pos - 1
    n = (pos + 1) if pos + 1 < len(A) else pos

    print(f'{pos}')

  return result


if __name__ == '__main__':
  main()
