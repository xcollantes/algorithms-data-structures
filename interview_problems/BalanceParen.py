"""Check if string has balanced parens."""

from typing import List

def main():
  s = '[]'
  s2 = '{}'
  s3 = '([])'
  s4 = '[(])'

  print(BalanceParen(s))
  print(BalanceParen(s2))
  print(BalanceParen(s3))
  print(BalanceParen(s4))
  print(BalanceParen(''))
  print(BalanceParen('['))


def BalanceParen(s: str) -> bool:
  if len(s) < 2:
    return False

  leftChars = ['(','[','{']
  rightChars = [')',']','}']
  stack = []

  for e in s:
    if e in leftChars:
      stack.append(e)
    if e in rightChars:
      if len(stack) == 0:
        return False
      else:
        last = stack.pop()

        if leftChars.index(last) == rightChars.index(e):
          return True
        else:
          return False
        

if __name__ == '__main__':
  main()
