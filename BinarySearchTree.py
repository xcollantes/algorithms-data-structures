"""Binary Search Trees Practice.
"""
__author__ = 'Xavier Collantes'

from BSTNode import BSTNode as Node

def main():
  bst = BinarySearchTree()
  bst.Put(100, 'Space')
  bst.Put(200, 'Nouget')
  bst.Put(300, 'Starman')
  bst.P()

  print(f'getting id: {bst.Get(200)}')

class BinarySearchTree:

  def __init__(self):
    self.root = None
    self.size = 0

  def Length(self):
    return self.size

  def P(self):
    self._print(self.root)

  def _print(self, current_node):
    print('%s | %s' % (current_node.key, current_node.data))
    if current_node.left:
      self._print(current_node.left)
    if current_node.right:
      self._print(current_node.right)

  def Put(self, key, value):
    if self.root:
      self._put(key, value, self.root)
    else:
      self.root = Node(key, data=value)
      self.size += 1




  def Get(self, key):
    """Find value of corresponding key.

    key: Unique ID of node in tree.
    Returns: Value of the node by key.
    """
    if self.root:
      return self._get(key, self.root)
    else:
      raise KeyError


  def _put(self, key, payload, current_node):
    if key < current_node.key:
      if current_node.left:
        self._put(key, payload, current_node.left)
      else:
        new_node = Node(key, data=payload)
        current_node.left = new_node
        self.size += 1

    if key >= current_node.key:
      if current_node.right:
        self._put(key, payload, current_node.right)
      else:
        new_node = Node(key, data=payload)
        current_node.right = new_node
        self.size += 1


  def _get(self, key, current_node):
    print("recur: ", current_node.data)
    if key < current_node.key:
      if current_node.left:
        print(f'on key: {current_node.key} L exists')
        return self._get(key, current_node.left)

    if key > current_node.key:
      if current_node.right:
        print(f'on key: {current_node.key} R exists')
        return self._get(key, current_node.right)

    if key == current_node.key:
      print(f'Match found {current_node.data}')
      return current_node.data
    else:
      raise KeyError(f'{key} Key not found :(')


if __name__ == '__main__':
  main()
