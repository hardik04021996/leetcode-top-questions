"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

from typing import Optional
from linked_list.easy.create_linked_list import ListNode


class Solution:
    def get_tail(self, head):
        if head is None:
            return None, 0
        current = head
        length = 1
        while current.next is not None:
            current = current.next
            length += 1
        return current, length

    def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail, length = self.getTail(head)
        if length <= 2:
            return head
        current = head
        index = 1
        while index < length:
            even_node = current.next
            current.next = current.next.next
            tail.next = even_node
            tail = tail.next
            tail.next = None
            current = current.next
            index += 2
        return head
    
    # Alternative canonical approach
    def odd_even_list_canonical(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Build odd and even sublists and then connect odd tail to even head. 
        It avoids having to compute the tail/length first.
        It is standard O(1) extra space / O(n) time solution
        """
        if head is None:
            return None
        odd = head
        even = head.next
        even_head = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head