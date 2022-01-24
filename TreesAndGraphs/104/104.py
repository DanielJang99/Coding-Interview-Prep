# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, length = stack.pop()
            if length > depth:
                depth = length
            if node.left:
                stack.append((node.left, length+1))
            if node.right:
                stack.append((node.right, length+1))
            
        return depth

#  Recursive solution - better runtime, more memory required 
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return self.dfs(root, 1)
    
#     def dfs(self, node, current_depth):
#         if not node or (not node.left and not node.right):
#             return current_depth
#         left_max = self.dfs(node.left, current_depth+1)
#         right_max = self.dfs(node.right, current_depth+1)
#         return max(left_max, right_max)