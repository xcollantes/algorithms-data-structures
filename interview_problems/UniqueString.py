"""Unique characters in string."""

from typing import List

def main():
  s = 'abbkdls'
  s2 = 'abcd'
  s3 = 'abcc'

  print(isAllUnique(s))


def isAllUnique(s: str) -> bool:
  seen = []
  for e in s:
    if e in seen:
      return False
    else:
      seen.append(e)

  return True

if __name__ == '__main__':
  main()
