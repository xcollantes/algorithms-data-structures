"""Implement Singly Linked List problems.
"""

__author__ = 'Xavier Collantes'

from LinkedList import Node
import copy

def main():
  # Build lists

  list_head = Node('genesis')
  ptr = list_head
  for b in range(50):
    ptr.next = Node(b)
    ptr = ptr.next


  # Copy and create circular list
  list_cir = copy.deepcopy(list_head)
  cir_ptr = list_cir
  while cir_ptr.next is not None:
    cir_ptr = cir_ptr.next

  cir_ptr.next = list_cir

  #p(list_cir)  # 1 Infinity Loop.... Cupertino California

  # Check if linked list is circular.
  print('CIR? %s' % is_circular(list_cir))
  print('TO REVERSE: ')
  p(list_head)
  print('IN REVERSE: ')
  p(Reverse(list_head))

  print('Nth to the Last')
  print(NthToLast(15, list_head))


def Reverse(in_head):
  """Reverse a linked list given a head.
  Waaaay better answer that keeps fixed space.
  """
  head = copy.deepcopy(in_head)
  current = head
  prev = None
  next = None

  while current:
    next = current.next
    current.next = prev

    prev = current
    current = next

  return prev


def NthToLast(n, head):
  """Return the nth to last node value.

  n: Nth to last node.
  head: First node of linked list.

  Return: Contents of last to Nth node.
  """
  current = head
  scout = current

  for i in range(n - 1):
    if scout.next == None:
      return scout.data
    else:
      scout = scout.next

  while scout.next:
    current = current.next
    scout = scout.next

  return current.data


def reverseBad(head):
  """Reverse a linked list given a head.
  Sub-par answer since this creates an intermediary linked
  list.
  """
  if head.data:
    out_list = Node(head.data)
  else:
    return 'Error'

  hptr = head
  optr = out_list
  print('head: ', head)
  print('olist: ', out_list)
  while hptr.next:
    temp_node = Node(hptr.next.data)
    temp_node.next = optr

    optr = temp_node
    hptr = hptr.next
  print('optr: ', optr)
  return optr


def is_circular(in_head):
  head = copy.deepcopy(in_head)

  p1 = head
  p2 = head.next
  while p2.next and p2.next.next is not None:
    print('P1: %s' % p1.data)
    print('P2: %s\n' % p2.data)
    if p1 == p2:
      print('Correctumundo: P1 %s P2 %s' % (p1.data, p2.data))
      return True
    else:
      p1 = p1.next
      p2 = p2.next.next

  return False






def p(list_head):
  """Printing for linked lists.
  """
  while list_head.next != None:
    print(list_head.data, end=' -> ')
    list_head = list_head.next

  print(list_head.data, end=' -> None\n')


if __name__ == '__main__':
  main()
