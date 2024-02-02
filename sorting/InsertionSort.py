#!/usr/bin/python2
"""Insertion Sort"""

def main():

  A = [5,4,2,1,3,0]
  print A

  for e in range(1, len(A) - 1):
    currIndex = e - 1
    target = e
    print 'e:{}  {} {} {}'.format(e, A[currIndex - 1], A[target], A[currIndex + 1])
    while A[currIndex - 1] > A[e] > A[currIndex + 1]:
      currIndex = currIndex - 1
      print 'currIndex dec:', currIndex
    A[currIndex], A[e] = A[e], A[currIndex]






  print A









if __name__ == '__main__':
  main()
