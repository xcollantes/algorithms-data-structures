# Trees Practice

__author__ = 'Xavier Collantes'

class BinaryTree:
  def __init__(self, root):
    self.root = root
    self.left = None
    self.right = None


  def PreOrder(self):
      print(self.root, '->', end=" ")
      if self.GetLeft():
        self.GetLeft().PreOrder()
      if self.GetRight():
        self.GetRight().PreOrder()


  def GetRight(self):
    return self.right


  def GetLeft(self):
    return self.left


  def SetRight(self, data):
    self.root = data


  def SetLeft(self, data):
    self.root = data


  def GetRoot(self):
    return self.root


  def SetRoot(self, data):
    self.root = data


  def InsertLeft(self, data):
    if self.left == None:
      self.left = BinaryTree(data)
    else:
      t = BinaryTree(data)
      t.left = self.left
      self.left = t


  def InsertRight(self, data):
    if self.right == None:
      self.right = BinaryTree(data)
    else:
      t = BinaryTree(data)
      t.right = self.right
      self.right = t
