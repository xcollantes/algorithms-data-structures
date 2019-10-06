"""Queue behavior with two stacks."""

from typing import List
import unittest

class Queue2Stacks:
  def __init__(self):
    self._stack1 = []
    self._stack2 = []
    self.size = 0

  def enqueue(self, element: int):
    self._stack1.append(element)
    self.size += 1

  def dequeue(self) -> int:
    for e in range(self.size - 1):
      last = self._stack1.pop()
      print(last)
      self._stack2.append(last)

    result = self._stack1.pop()
    self.size -= 1
    print(f'RESULT: {result}')
    for i in range(self.size):
      self._stack1.append(self._stack2.pop())

    return result



class Queue2StacksTest(unittest.TestCase):
  def testRun(self):
    q = Queue2Stacks()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    self.assertEqual(q.dequeue(), 0)
    self.assertEqual(q.dequeue(), 1)
    self.assertEqual(q.dequeue(), 2)
    self.assertEqual(q.dequeue(), 3)


if __name__=='__main__':
  unittest.main()
