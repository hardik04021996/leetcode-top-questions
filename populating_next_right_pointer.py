# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while(queue):
            levelsize = len(queue)
            prev = None
            for _ in range(levelsize):
                node = queue[0]
                queue = queue[1:]
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

# Example usage
sol = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
connected_root = sol.connect(root)

def safe_print(node):
    print(node.val if node else None)

safe_print(connected_root.left.next)  # Output: 3
safe_print(connected_root.left.left.next)  # Output: 5
safe_print(connected_root.left.right.next)  # Output: 6
safe_print(connected_root.right.right.next)  # Output: None (as it's the last node in its level)
safe_print(connected_root.next)  # Output: None (as root is the first node)
safe_print(connected_root.left.next)  # Output: 3 (2's next is 3)
safe_print(connected_root.right.next)  # Output: None (3's next is None)
