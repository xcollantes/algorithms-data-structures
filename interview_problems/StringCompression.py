"""Array manipulation problem."""

from typing import List

def main():
  s = 'AAABBBCDEFFF'
  print(f'{s} -> {compression(s)}')


def compression(text: str) -> str:
  currLetterCount = 0
  resultStr = ''

  posLast = 0
  pos = 1
  while pos <= len(text) - 1:
    currLetterCount += 1
    print(f'{currLetterCount}  {text[posLast]} - {text[pos]}  {resultStr}')
    if text[posLast] != text[pos]:
      resultStr += text[posLast] + str(currLetterCount)
      currLetterCount = 0

    posLast += 1
    pos += 1

  resultStr += text[posLast] + str(currLetterCount + 1)
  return resultStr


if __name__=='__main__':
  main()
