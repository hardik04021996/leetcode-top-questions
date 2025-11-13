"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
There are no cycles anywhere in the entire linked structure.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_intersection_node(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        traversed = set()
        currentA = headA
        currentB = headB
        while currentA is not None:
            traversed.add(currentA)
            currentA = currentA.next
        while currentB is not None:
            if currentB in traversed:
                return currentB
            currentB = currentB.next
        return
    
    # Alternative two-pointer solution
    def get_intersection_node_two_pointer(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Two-pointer solution to find the intersection node of two linked lists.

        Approach summary:
        - Use two pointers, `ptrA` and `ptrB`, starting at the heads of
          lists A and B respectively.
        - Move each pointer one step at a time. When a pointer reaches the
          end of its list, redirect it to the head of the other list.
        - If there is an intersection, the pointers will meet at the
          intersection node after at most 2 passes through the lists.
        - If there is no intersection, both pointers will eventually be None
          at the same time.

        Example: headA=[4,1,8,4,5], headB=[5,0,1,8,4,5]
          - Pointers traverse their lists and switch heads upon reaching
            the end. They meet at node with value 8.

        Complexity: O(M+N) time, O(1) extra space.
        """
        if headA is None or headB is None:
            return None
        
        ptrA = headA
        ptrB = headB
        
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA is not None else headB
            ptrB = ptrB.next if ptrB is not None else headA
        
        return ptrA  # Can be intersection node or None

    # Alternative version of two-pointer solution which is equivalent to above but slightly easier to reason about and readable.
    def get_intersection_node_alternative(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == headB:
            return headA
        currentA = headA
        currentB = headB
        while currentA is not None or currentB is not None:
            if currentA == currentB:
                return currentA

            if currentA is not None:
                currentA = currentA.next
            else:
                currentA = headB

            if currentB is not None:
                currentB = currentB.next
            else:
                currentB = headA
        return