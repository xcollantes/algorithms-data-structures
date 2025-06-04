"""61. Rotate List

Medium

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


def test_rotate_linked_list():
    """pytest rotate_linked_list.py"""
    # Test case 1: [1,2,3,4,5], k = 2
    head1 = create_linked_list([1, 2, 3, 4, 5])
    expected1 = create_linked_list([4, 5, 1, 2, 3])
    result1 = rotate_linked_list(head1, 2)
    assert linked_list_to_list(result1) == linked_list_to_list(expected1)

    # Test case 2: [0,1,2], k = 4
    head2 = create_linked_list([0, 1, 2])
    expected2 = create_linked_list([2, 0, 1])
    result2 = rotate_linked_list(head2, 4)
    assert linked_list_to_list(result2) == linked_list_to_list(expected2)

    # Test case 3: [], k = 0
    assert rotate_linked_list(None, 0) is None

    # Test case 4: [1], k = 1
    head4 = create_linked_list([1])
    result4 = rotate_linked_list(head4, 1)
    assert linked_list_to_list(result4) == [1]

    # Test case 5: [1,2], k = 2
    head5 = create_linked_list([1, 2])
    expected5 = create_linked_list([1, 2])
    result5 = rotate_linked_list(head5, 2)
    assert linked_list_to_list(result5) == linked_list_to_list(expected5)


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


def linked_list_to_list(head):
    """Helper function to convert a linked list to a list for comparison."""
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


class ListNode:
    """ListNode"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_linked_list(head: ListNode, k: int) -> ListNode:
    """"""
    if not head or k == 0:
        return head

    h = head
    length = 1
    c = h

    # Get tail.
    # Need tail because should not iterate through whole list for each move.
    while c.next:
        length += 1
        c = c.next

    t = c
    t.next = h

    m = length - (k % length)
    print(f"m {m}")
    for i in range(m):
        print(f"rotate: {i}")
        c = c.next

    t = c
    h = t.next
    t.next = None

    print(f"answer")
    p(h)

    return h


def p(h: ListNode):
    while h:
        print(f"val: {h.val}")
        h = h.next


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.LINKED_LIST, Tags.TWO_POINTERS],
    difficulty=Difficulty.MEDIUM,
)
