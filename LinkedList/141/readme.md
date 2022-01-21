141. Linked List Cycle (#Easy)

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the _next_ pointer. Internally, _pos_ is used to denote the index of the node that tail's _next_ pointer is connected to. Note that **pos is not passed as a parameter.**

Return _true_ if there is a cycle in the linked list. Otherwise, return _false_.

**Example 1**

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Example 2**

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

**Example 1**

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```
