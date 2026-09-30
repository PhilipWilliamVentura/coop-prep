# Pattern: Iteration using stack
# Time: O(n) | Space: O(n)
# Tripped up on: Use a stack and keep going left while appending root.
#                If root is none, root = stack.pop(), check if k == 0 and go right once.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if 0 == k:
                return root.val
            root = root.right