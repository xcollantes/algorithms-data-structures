"""Finding the middle of a linked list."""

from typing import Any


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None


def array_to_linked_list(arr: list) -> Node:
    head = Node(arr[0])
    c = head

    for e in arr[1:]:
        c.next = Node(e)
        c = c.next

    return head


def pp(h):
    while h:
        print(f"{h.val} -> ", end="")
        h = h.next
    print(f"N")


head = array_to_linked_list([x for x in range(20)])

pp(head)

slow = head
fast = head

while fast and fast.next:
    print(f"SLOW {slow.val} FAST {fast.val}")
    slow = slow.next
    fast = fast.next.next

print(f"MID {slow.val}")






