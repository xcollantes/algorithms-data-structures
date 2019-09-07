"""Binary Search Trees Practice.
"""
__author__ = 'Xavier Collantes'


class BSTNode:
  def __init__(self, key, data=None):
    self.key = key
    self.data = data
    self.left = None
    self.right = None

  def GetRight(self):
    return self.right

  def GetLeft(self):
    return self.left

  def SetRight(self, data):
    self.data = data

  def SetLeft(self, data):
    self.data = data

  def GetKey(self):
    return self.key

  def GetData(self):
    return self.data


