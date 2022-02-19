# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
        output = [{"count":0, "sum":0}]
        def dfs(node, depth):
            if depth < len(output):
                output[depth]["count"] += 1
                output[depth]["sum"] += node.val
            else:
                output.append({"count":1, "sum":node.val})
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
        dfs(root, 0)
                
        return [(level["sum"] / level["count"]) for level in output]

