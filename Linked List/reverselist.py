# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# I believe this is the recursive solution?
class Solution:
    def reverseList(self, head):
        pointer = head
        prev = None
        while pointer is not None:
            oldnext = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = oldnext
        return prev

