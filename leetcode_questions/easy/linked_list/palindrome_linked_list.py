"""234. Palindrome Linked List

Easy

Given the head of a singly linked list, return true if it is a palindrome or
false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from leetcode_questions.utils.linked_list import ListNode, create_linked_list, pp


def test_palindrome_linked_list():
    """pytest palindrome_linked_list.py"""
    assert is_palindrome(create_linked_list([1, 2, 2, 1])) == True
    # assert is_palindrome(create_linked_list([1, 2])) == False
    # assert is_palindrome(create_linked_list([1])) == True


def is_palindrome(head: ListNode) -> ListNode:

    def reverse(head: ListNode):
        """Reverse the linked list."""

        p = None  # Start with None since new tail will point to None.
        c = head

        while c:
            # 1. n is treated as a temp node.
            # c will be disconnected to next node so n keeps where c will be.
            n = c.next

            # 2. Wire next to the prev.
            c.next = p

            # 3. Increment prev to +1.
            p = c

            # 4. Move current node to next.
            c = n

        # Prev is now the new head since the list is singly linked and reversed.
        # Starting from a fixed head from beginning will have nowhere to go.

        pp(p)
        return p

    # traverse both the original and reversed.
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    rev = reverse(slow)

    while rev:
        print(f"h: {head.val} rev: {rev.val}")
        if head.val != rev.val:
            return False

        head = head.next
        rev = rev.next

    return True


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.LINKED_LIST, Tags.TWO_POINTERS, Tags.STACK, Tags.PALINDROME],
    difficulty=Difficulty.EASY,
)
