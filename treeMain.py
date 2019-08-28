#!/env/bin/python3


from BinaryTree import BinaryTree

def main():
  tree = BinaryTree('zero')
  tree.InsertLeft('a')
  tree.InsertRight('b')

  print(tree.GetRoot())
  print('left: ', tree.GetLeft())
  print('right: ', tree.GetRight())

  TreeChapters()

#  my_tree = BinaryTree('seed')
#  my_tree.InsertLeft('leftSeed')
#  my_tree.InsertRight('rightSeed')
#  print(my_tree.GetRoot())

def TreeChapters():
  """Initalizes a b-tree with data as book chapters, sub-chapters, etc.
  Create tree with chapters then traverse PRE-ORDER.
  """
  chapters = [1, 2, 5, 3, 8, 6, 10, 4]
  book = BinaryTree(chapters[0])

  for c in chapters[1:]:
    temp_book = BinaryTree(c)
    if c < book.GetRoot():
      book.InsertLeft(c)
    else:
      book.InsertRight(c)

  book.PreOrder()


if __name__ == '__main__':
  main()










