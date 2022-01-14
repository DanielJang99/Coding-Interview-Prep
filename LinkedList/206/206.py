# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:

    # recursive solution 
    if not head or not head.next:
        return head
    node = reverseList(head.next)
    head.next.next = head
    head.next = None
    return node
    

    # iterative solution 
    # current = head
    # prev = None
    # while(current):
    #     n = current.next
    #     current.next = prev
    #     prev = current 
    #     current = n
        
    # return prev
        