# Superbalanced Tree

Write a function to see if a binary tree is "superbalanced".

A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

Here's a sample binary tree node class:

```
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
```

# Binary Search Tree

Write a function to check that a binary tree is a valid **binary search tree**.

A binary search tree is a binary tree where the nodes are ordered in a specific way. For every node:

-   The nodes to the left are smaller than the current node.
-   The nodes to the right are larger than the current node.
