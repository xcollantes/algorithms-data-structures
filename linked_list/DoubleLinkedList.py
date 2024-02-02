"""Implementation of Doublely Linked List.
"""

from LinkedList import Node

class DoubleNode(Node):
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
