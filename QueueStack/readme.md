# Largest Stack

You want to be able to access the largest element in a **stack.**

You've already implemented this Stack class:

```
class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]
```

Use your Stack class to **implement a new class MaxStack with a method get_max() that returns the largest element in the stack.** get_max() should not remove the item.

Your stacks will contain only integers. You should be able to get a runtime of O(1) for push(), pop(), and get_max().

# Queue with 2 Stacks

Implement a queue with 2 stacks. Your queue should have an enqueue and a dequeue method and it should be "first in first out" (FIFO).

Optimize for the time cost of mm calls on your queue. These can be any mix of enqueue and dequeue calls.

Assume you already have a stack implementation and it gives O(1) time push and pop.

# Paranthesis Matching

I like parentheticals (a lot).

"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).

# Bracket Validator

Let's say:

-   '(', '{', '[' are called "openers"
-   ')', '}', ']' are called "closers"

Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
Examples:

-   "{ [ ]() }" should return True
-   "{ [ ( ] ) }" should return False
-   "{ [ }" should return False
