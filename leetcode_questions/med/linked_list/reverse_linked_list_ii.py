"""92. Reverse Linked List II

Medium

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.


Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def test_reverse_linked_list_ii():
    """pytest reverse_linked_list_ii.py"""
    # The list is 1 -> 2 -> 3 -> 4 -> 5 and we reverse the sublist from positions 2 to 4.
    # Expected: 1 -> 4 -> 3 -> 2 -> 5.
    assert reverse_linked_list_ii(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4
    ) == ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
    # Single element list and reversing from 1 to 1 should return the same list.
    assert reverse_linked_list_ii(ListNode(5), 1, 1) == ListNode(5)


def reverse_linked_list_ii(head: ListNode, left: int, right: int) -> ListNode:
    # Early exit if the list is empty or the requested range is of length 1.
    if head is None or left == right:
        return head

    # Create a dummy node to simplify edge cases where reversal starts at the head.
    temp = ListNode(None, head)
    # `prev` will end up pointing to the node immediately before the `left` position.
    prev = temp

    # Advance `prev` to the node just before the start of the reversal segment.
    for i in range(left - 1):
        prev = prev.next

    # `cur` points to the first node in the segment that will be reversed.
    cur = prev.next

    # Perform in-place sublist reversal using head-insertion technique.
    # Repeatedly take the node after `cur` and insert it right after `prev`.
    for i in range(right - left):
        n = cur.next  # Node to move to the front of the reversed portion.
        # Rewire pointers in one tuple assignment to avoid temporary breakage.
        # After this, `n` becomes the new node immediately after `prev`.
        cur.next, n.next, prev.next = n.next, prev.next, n

    # Return the head of the updated list, skipping the dummy node.
    return temp.next
