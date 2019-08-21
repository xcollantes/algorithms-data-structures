
# Array Sequence Practice


def main():
  print('Anagram Check, Solution 1: %s' % anagram_check('clint eastwood', 'old west action'))
  print('Anagram Check, Solution 2: %s' % anagram_check2('clint eastwood', 'old west action'))
  print('Array Pairs, Solution 1: %s' % array_pair([1, 3, 2, 2], 4))

def array_pair(arr, sum):
  """Find the pairs in given array that sum up to the given sum.
  """
  eval = []
  for col in arr:
    for row in arr:
      if ((col + row) == sum) and ([col, row] not in eval) :
        eval.append([col, row])

  return eval


def anagram_check(x, y):
  ''' Anagram Check:  Check to see if both inputs are anagrams of each other. 
      Solution 1: Sort strings then compare since both should have the same 
      number of letters. 
  '''
  x = x.replace(' ', '').lower()
  y = y.replace(' ', '').lower()

  return sorted(x) == sorted(y)


def anagram_check2(x, y):
  '''Solution 2: Verify two inputs are anagrams.  
  '''
  x = x.replace(' ', '').lower()
  y = y.replace(' ', '').lower()

  if len(x) is not len(y):
    return False

  countDict = {}
  for a in x:  #  Loop first word
    if a in countDict:
      countDict[a] = countDict[a] + 1
    else:
      countDict[a] = 1

  print(countDict)

  for b in y:
    if b in countDict:
      countDict[b] = countDict[b] - 1
    else:
      return False

    if countDict[b] == 0:
      countDict.pop(b)
    if len(countDict) == 0:
      return True
    #print(countDict)
    #print(len(countDict))









if __name__=='__main__':
  main()
