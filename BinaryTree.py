"""Binary Trees Practice.
"""


__author__ = 'Xavier Collantes'

class BinaryTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


  def PreOrder(self):
      print(self.data, '->', end=" ")
      if self.GetLeft():
        self.GetLeft().PreOrder()
      if self.GetRight():
        self.GetRight().PreOrder()


  def GetRight(self):
    return self.right


  def GetLeft(self):
    return self.left


  def SetRight(self, data):
    self.data = data


  def SetLeft(self, data):
    self.data = data


  def GetData(self):
    return self.data


  def SetData(self, data):
    self.data = data


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
