
from typing import List

def main():
  print(fib_rec(6))
  print(fib_iter(6))

def fib_memo(n: int) -> int:






def fib_iter(n: int) -> int:
  a = 0
  b = 1
  for i in range(n):
    temp = b
    b = a + b
    a = temp

  return a


def fib_rec(n: int) -> int:
  if n == 1 or n == 0:
    return n
  else:
    return fib_rec(n - 2) + fib_rec(n - 1)


if __name__=='__main__':
  main()
