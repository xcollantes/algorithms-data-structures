"""Return all permutations of given string."""

import unittest
from typing import List


def perm(text: str) -> List[str]:
  out = []
  if len(text) == 0:
    out = [text]
  else:
    for i,letter in enumerate(text):
      print(f'ENUM: {i} {letter}')
      for permy in perm(text[:i] + text[i + 1:]):

        out += [letter + permy]
        #print(f'i: {i}  letter: {letter}')
  print(f'{out}\n')
  return out


def main():
  s = 'abc'
  print(perm(s))


if __name__=='__main__':
  #unittest.main()
  main()
