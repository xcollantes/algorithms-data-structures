
import random

def main():
  list = [random.randint(-10, 10) for _ in range(10)]
  print(list)

  m = len(list) - 1
  pos = 0

  while m > 0:
    print(f'PRE: {list}')

    n = 1
    currMax = list[0]
    for e in range(m):

      print(list[e])
      if list[e] > currMax:
        temp = currMax
        currMax = list[e]
        list[e] = temp

    list[m] = currMax
    print(f'MAX: {list[m]}')
    m -= 1

    print(f'POST: {list}')
  print(list)



if __name__ == '__main__':
  main()
