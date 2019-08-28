# Implementation of Stacks

__author__ = 'Xavier Collantes'

from Stack import Stack

def main():
  s = Stack()
  print('Empty?: %s' % s.IsEmpty())
  s.Push('Dazed and Confused')
  s.Push('I Can\'t Quit You Baby')
  s.Push('Wearing and Tearing')
  print(s.Peek())
  print(s.Peek())
  print('Size: %s' % s.Size())
  s.Pop()

  print('Size: %s' % s.Size())




if __name__=='__main__':
  main()
