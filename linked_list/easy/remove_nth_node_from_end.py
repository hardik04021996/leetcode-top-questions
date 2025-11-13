"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_length(self, head):
        curr = head
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.get_length(head)
        i = length - n
        counter = 0
        curr = head
        if i == 0:
            head = curr.next
            return head
        while curr is not None:
            counter += 1
            if counter == i:
                curr.next = curr.next.next
                return head
            else:
                curr = curr.next

    # Alternative one-pass solution using two pointers
    def remove_nth_from_end_one_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        One-pass (two-pointer) solution to remove the nth node from the end.

        Approach summary:
        - Create a dummy node that points to head. This simplifies deleting
          the head node itself when needed.
        - Use two pointers (`first` and `second`) starting at the dummy.
        - Advance `first` by n+1 steps so there is a gap of n nodes between
          `first` and `second`.
        - Move both pointers together until `first` reaches the end. At that
          point `second` is the node immediately before the node to remove.
        - Skip the target node via `second.next = second.next.next` and
          return `dummy.next`.

        Example: head=[1,2,3,4,5], n=2
          - After advancing `first` n+1 steps it points at value 3.
          - Moving both until `first` is None leaves `second` at value 3
            (node before 4). Removing `second.next` removes 4 -> result [1,2,3,5].

        Complexity: O(L) time, O(1) extra space.
        """
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next
