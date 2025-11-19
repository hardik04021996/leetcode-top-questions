"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list2.val < list1.val:
            list1, list2 = list2, list1
        current1, current2 = list1, list2
        while current1.next is not None:
            next_node1 = current1.next
            if current2 and next_node1 and current2.val < next_node1.val:
                next_node2 = current2.next
                current1.next = current2
                current2.next = next_node1
                current2 = next_node2
            current1 = current1.next
        current1.next = current2
        return list1