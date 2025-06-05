from typing import Any


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def create_linked_list(arr: list[Any]):
    """Initiate singly-linked list."""
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


def pp(head: ListNode):
    """Read linked list."""
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print("N")
    
