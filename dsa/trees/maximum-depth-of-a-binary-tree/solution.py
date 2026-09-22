# Pattern: Depth for Search (recursion)
# Time: O(n) | Space: O(h) height of the tree
# Tripped up on: straight forward problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))