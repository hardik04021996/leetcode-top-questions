"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(self, root, minimum = float('-inf'), maximum = float('inf')):
    if root is None:
        return True
    if root.val <= minimum or root.val >= maximum:
        return False
    is_left_bst = self.helper(root.left, minimum, root.val)
    is_right_bst = self.helper(root.right, root.val, maximum)
    return is_left_bst and is_right_bst

def isValidBST(self, root: TreeNode) -> bool:
    return self.helper(root)
