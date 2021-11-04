# Definition for singly-linked list provided by LeetCode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Bag:
    def __init__(self):
        self.head = None;
        self.tail = self.head

    def add(self, value):
        toadd = ListNode(value)
        
        if self.tail is not None:
            self.tail.next = toadd
        else:
            self.head = toadd

        self.tail = toadd
        
class Solution:
    def mergeTwoLists(self, l1, l2):
        i = l1
        j = l2
        bag = Bag()

        while True:
            if i is None and j is None:
                break
            if i is None:
                bag.add(j.val)
                j = j.next
            elif j is None:
                bag.add(i.val)
                i = i.next
            elif i.val <= j.val:
                bag.add(i.val)
                i = i.next
            elif i.val > j.val:
                bag.add(j.val)
                j = j.next

        return bag.head