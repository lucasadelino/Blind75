# Definition for singly-linked list provided by LeetCode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> 'bool':
        """Use a set to keep track of object ids, and a counter that increases
        everytime a node is visited. If there is a discrepancy between the
        counter and the length of set elements, it means we just tried to add 
        the ID of a node."""
        setids = set()
        pointer = head
        counter = 0
        while True:
            if pointer is None:
                return False
                
            setids.add(id(pointer))
            counter += 1
            if counter > len(setids):
                return True
            pointer = pointer.next
