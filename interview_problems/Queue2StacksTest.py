"""Test Queue2Stack class."""

import unittest
from Queue2Stacks import Queue2Stacks

class Queue2StackTest(unittest.TestCase):
  def setUp(self):
    print(f'SETUP: Starting Test')

  def tearDown(self):
    print('TEARDOWN')

  def testEnqueue(self):
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
