from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return -1
            depth_left = dfs(node.left)
            depth_right = dfs(node.right)
            self.diameter = max(self.diameter, depth_left+depth_right+2)
            return max(depth_left, depth_right)+1
        
        dfs(root)
        return self.diameter
        