# Definition for singly-linked list provided by LeetCode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creates bag data structure to make it easier to add elements
class Bag:
    def __init__(self):
        self.head = None;
        self.tail = self.head

    def add(self, value):
        toadd = ListNode(value)

        # Prevent accessing None (for adding 1st element when the bag is empty)
        if self.tail is not None:
            self.tail.next = toadd
        # But if the bag was empty, set the element we just added as the head
        else:
            self.head = toadd
        
        self.tail = toadd
        
class Solution:
    def mergeTwoLists(self, l1, l2):
        """Creates a new list. Uses two pointers i and j to compare elements. 
        Use the comparison to populate the new list and move pointers 
        accordingly"""
        i = l1
        j = l2
        bag = Bag()

        # Iterate over l1 and l2
        while True:
            # If this happens, we've reached the end of both argument lists
            if i is None and j is None:
                break

            # If one pointer is None but the other isn't, use the other
            if i is None:
                bag.add(j.val)
                j = j.next
            elif j is None:
                bag.add(i.val)
                i = i.next

            # Compare non-None values
            elif i.val <= j.val:
                bag.add(i.val)
                i = i.next
            elif i.val > j.val:
                bag.add(j.val)
                j = j.next

        return bag.head