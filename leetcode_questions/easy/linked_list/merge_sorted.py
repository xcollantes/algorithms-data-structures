"""21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    result_head = ListNode(0)
    result = result_head

    while list1 and list2:
        if list1.val <= list2.val:
            result.next = ListNode(list1.val)
            result = result.next

            list1 = list1.next
        else:
            result.next = ListNode(list2.val)
            result = result.next

            list2 = list2.next

    while list1:
        result.next = ListNode(list1.val)
        result = result.next
        list1 = list1.next

    while list2:
        result.next = ListNode(list2.val)
        result = result.next
        list2 = list2.next

    return result_head.next
