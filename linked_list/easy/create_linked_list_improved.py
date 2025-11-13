"""
Improved Linked List Implementation: Avoiding Redundant Arguments

PROBLEM with the original approach:
    head.add(head, a[i])
    head.delete(head, b[i])

When you call head.add(head, a[i]), you're passing 'head' twice:
1. Once implicitly as 'self' (because you're calling a method on the head object)
2. Once explicitly as the first argument 'head'

This is redundant! Python automatically passes the object you call the method on
as the 'self' parameter. You don't need to pass it again.

SOLUTION: Use a separate LinkedList class that manages the head pointer.
This way, methods operate on the list structure itself, not on individual nodes.
"""

class ListNode:
    """Represents a single node in the linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    """
    A LinkedList class that manages the entire list.
    This avoids passing 'head' as an argument to every method.
    """
    def __init__(self, head_value=None):
        """Initialize with an optional head value."""
        self.head = ListNode(head_value) if head_value is not None else None

    def add(self, x):
        """
        Add a value to the end of the list.
        NO NEED to pass head as argument—self.head is already available!
        """
        if self.head is None:
            self.head = ListNode(x)
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = ListNode(x)

    def delete(self, x):
        """
        Delete all nodes with value x from the linked list.
        The head is managed internally via self.head.
        """
        # Handle deletion of head node(s)
        while self.head is not None and self.head.val == x:
            print(f"deleting {x} from head")
            self.head = self.head.next

        # Handle deletion in the rest of the list
        if self.head is None:
            return

        current = self.head
        while current.next is not None:
            if current.next.val == x:
                print(f"deleting {x}")
                current.next = current.next.next
            else:
                current = current.next

    def print_list(self):
        """
        Print all values in the list.
        Again, no need to pass head—we use self.head internally!
        """
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next


# ============ USAGE EXAMPLE ============
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [5, 7]

# Create LinkedList with first element
linked_list = LinkedList(a[0])

# Add remaining elements - much cleaner! No redundant 'head' argument
print("--- Creating list ---")
for i in range(1, len(a)):
    linked_list.add(a[i])

print("--- Original list ---")
linked_list.print_list()

# Delete elements - clean API, no redundant arguments
print("\n--- Deleting elements ---")
for i in range(len(b)):
    linked_list.delete(b[i])

print("\n--- Final list ---")
linked_list.print_list()

"""
KEY DIFFERENCES:

Original approach:
    head.add(head, a[i])              # Redundant: head passed twice
    head.delete(head, b[i])           # Redundant: head passed twice

Improved approach:
    linked_list.add(a[i])              # Clean: head managed internally
    linked_list.delete(b[i])           # Clean: head managed internally

WHY THIS IS BETTER:
1. No redundant arguments - the list manages its own head
2. Cleaner API - method calls are simpler and more intuitive
3. Safer - the head is encapsulated within the LinkedList class
4. More Pythonic - follows standard patterns used in collections
5. Easier to extend - if you need more operations, they all have access to self.head
"""
