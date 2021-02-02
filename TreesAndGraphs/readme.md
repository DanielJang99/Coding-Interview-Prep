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

# Second Largest Item

Write a function to find the 2nd largest element in a **binary search tree**.

# Graph Coloring

Given an undirected graph with maximum degree D, find a graph coloring using at most D+1 colors.

Graphs are represented by a list of N node objects, each with a label, a set of neighbors, and a color:

```
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
```
