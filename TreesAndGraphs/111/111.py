# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    depth = 1
    queue = [(root, depth)]
    while(queue):
        node, d = queue.pop(0)
        if not node.left and not node.right:
            return d
        if(node.left): 
            queue.append((node.left, d+1))
        if (node.right):
            queue.append((node.right, d+1))
    return depth