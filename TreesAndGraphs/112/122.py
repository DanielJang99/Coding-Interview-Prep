# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    val = 0 
    stack = [(root, val)]
    while(stack):
        node, value = stack.pop()
        value += node.val
        if not node.left and not node.right and value == targetSum:
            return True
        if (node.left):
            stack.append((node.left, value))
        if (node.right):
            stack.append((node.right, value))
    return False

