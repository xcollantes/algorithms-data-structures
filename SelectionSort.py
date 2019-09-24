
import random

def main():
  list = [random.randint(-10, 10) for x in range(10)]
  print(list)

  m = len(list)
  pos = 0

  while m > 0:
    print(f'PRE: {list}')

    for e in range(2, m):
      print(e)
      if list[e - 1] > list[e]:
        temp = list[e - 1]
        list[e - 1] = list[e]
        list[e] = temp

    m -= 1

    print(f'POST: {list}')
  print(list)



if __name__ == '__main__':
  main()
