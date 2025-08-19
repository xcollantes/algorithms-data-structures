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

    def __eq__(self, other):
        """Compare two linked lists structurally."""
        if not isinstance(other, ListNode):
            return False

        current_self = self
        current_other = other

        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next

        # Both should be None at the end for equality.
        return current_self is None and current_other is None


def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test_reverse_linked_list_ii():
    """pytest reverse_linked_list_ii.py"""
    # The list is 1 -> 2 -> 3 -> 4 -> 5 and we reverse the sublist from positions 2 to 4.
    # Expected: 1 -> 4 -> 3 -> 2 -> 5.
    assert reverse_linked_list_ii(
        create_linked_list([1, 2, 3, 4, 5]), 2, 4
    ) == create_linked_list([1, 4, 3, 2, 5])

    # Single element list and reversing from 1 to 1 should return the same list.
    assert reverse_linked_list_ii(create_linked_list([5]), 1, 1) == create_linked_list(
        [5]
    )


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

        # The cur node will stay stationary while the next value moves.
        cur.next, n.next, prev.next = n.next, prev.next, n

    print(cur.val)

    # Return the head of the updated list, skipping the dummy node.
    return temp.next
