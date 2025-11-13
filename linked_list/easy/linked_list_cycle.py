"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def has_cycle(self, head: Optional[ListNode]) -> bool:
        traversed = set()
        current = head
        while current is not None:
            if current in traversed:
                return True
            else:
                traversed.add(current)
            current = current.next
        return False

    # Alternative Floyd's Tortoise and Hare algorithm
    def has_cycle_floyd(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False