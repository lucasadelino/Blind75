# Definition for singly-linked provided by LeetCode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative solution
class Solution:
    def reverseList(self, head):
        """
        Iterates through the list, saving references to the previous element,
        and setting the .next of the current element to the previous element.
        """
        pointer = head
        prev = None
        while pointer is not None:
            # Create a new reference to pointer.next, because we will change 
            # where pointer.next points to, but we also need the original 
            # reference to continue to iterate
            oldnext = pointer.next
            
            pointer.next = prev
            prev = pointer
            pointer = oldnext
        return prev

