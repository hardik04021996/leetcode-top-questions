"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current is not None:
            stack.append(current.val)
            current = current.next
        current = head
        while current is not None:
            current.val = stack.pop()
            current = current.next
        return head
    
    # Alternative in-place iterative solution
    def reverse_list_in_place(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            next_node = current.next  # Store next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev to current
            current = next_node       # Move to next node
        return prev  # New head of the reversed list
    
    # Alternative recursive solution
    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head