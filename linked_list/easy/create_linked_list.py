"""
Given 2 arrays:
Create a linked list from 1st array
Then delete elements in 2nd array from linked list
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, head, x):
        while head.next is not None:
            head = head.next
        head.next = ListNode(x)
        return
    
    def delete(self, head, x):
        """
        Delete all nodes with value x from the linked list.
        Returns the head of the modified list (important if head is deleted).
        """
        # Handle deletion of head node(s)
        while head is not None and head.val == x:
            print(f"deleting {x} from head")
            head = head.next
        
        # Handle deletion in the rest of the list
        if head is None:
            return head
        
        current = head
        while current.next is not None:
            if current.next.val == x:
                print(f"deleting {x}")
                current.next = current.next.next
            else:
                current = current.next
        
        return head

    def print_list(self, head):
        current = head
        while current is not None:
            print(current.val)
            current = current.next
        return

a = [1,2,3,4,5,6,7,8]
b = [5,7]

head = ListNode(a[0])

for i in range(1,len(a)):
    head.add(head, a[i])

head.print_list(head)

print("\n--- Deleting elements ---")
for i in range(0, len(b)):
    head = head.delete(head, b[i])

print("\n--- Final list ---")
head.print_list(head)
