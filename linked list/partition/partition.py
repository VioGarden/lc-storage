# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x):
        buffer1, buffer2 = ListNode(0), ListNode(0)
        b1, b2 = buffer1, buffer2

        while head:
            if head.val < x:
                b1.next, b1 = head, head
            else:
                b2.nex, b2 = head, head
            head = head.next
        
        
        b1.next = buffer2.next
        b2.next = None
        return buffer1.next