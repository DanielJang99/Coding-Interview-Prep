from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    walker, runner = head, head
    while runner and runner.next:
        walker = walker.next 
        runner = runner.next.next
        if walker == runner:
            return True
    return False
