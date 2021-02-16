# Delete Node

Delete a node from a singly-linked list, given only a variable pointing to that node.

The input could, for example, be the variable b below:

```
class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
```

# Linked List Cycle

You have a singly-linked list and want to check if it contains a cycle.
A singly-linked list is built with nodes, where each node has:

-   node.next: the next node in the list.
-   node.value: the data held in the node. For example, if our linked list stores people in line at the movies, node.value might be the person's name.

A cycle occurs when a node’s next points back to a previous node in the list. The linked list is no longer linear with a beginning and end—instead, it cycles through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.

We can do this in O(n)O(n) time and O(1)O(1) space!

# Reverse a linked list

Write a function for reversing a linked list. Do it in place.

Your function will have one input: the head of the list.

Your function should return the new head of the list.

# Kth to last node in a singly linked list

You have a linked list and want to find the kth to last node.

Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the kth to last node in the list.

For example:

```
  class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
kth_to_last_node(2, a)
```
