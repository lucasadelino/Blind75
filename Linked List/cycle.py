# Definition for singly-linked list provided by LeetCode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> 'bool':
        """Use a set to keep track of object ids. If we try to add another 
        element, then there is a cycle"""
        objset = set()
        pointer = head
        while True:
            if pointer is None:
                return False
            if pointer in objset:
                return True
            else:
                objset.add(pointer)
            pointer = pointer.next
            
