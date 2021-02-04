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

# Find a duplicate

We are given a list where:

1. the integers are in the range 1..n
2. the list has a length of n+1

We can find a duplicate integer in O(n) time while keeping our space cost at O(1).

This is a tricky one to derive (unless you have a strong background in graph theory), so we'll get you started:

**Imagine each item in the list as a node in a linked list.** In any linked list, each node has a value and a **"next"** pointer. In this case:

-   The value is the integer from the list.
-   The "next" pointer points to the value-eth node in the list (numbered starting from 1). For example, if our value was 3, the "next" node would be the third node.

**Notice we're using "positions" and not "indices."** For this problem, we'll use the word "position" to mean something like "index," but different: indices start at 0, while positions start at 1. More rigorously: position = index + 1.

Using this, find a duplicate integer in O(n) time while keeping our space cost at O(1)O(1).
