"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        listed = []
        while current is not None:
            listed.append(current.val)
            current = current.next
        left = 0
        right = len(listed)-1
        while left < right:
            if listed[left] != listed[right]:
                return False
            left += 1
            right -= 1
        return True

    # Alternative approach using fast and slow pointers to find the middle, reverse the second half, and compare
    def is_palindrome_optimized(self, head: Optional[ListNode]) -> bool:
        # Find middle
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        current = slow
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Compare first and second half
        first_half = head
        second_half = prev
        while second_half is not None:
              if first_half.val != second_half.val:
                    return False
              first_half = first_half.next
              second_half = second_half.next
        return True
