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
