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
            curr = head.next
            if head.val < x:
                buffer1.next = head
                buffer1 = buffer1.next
                head.next = None
                head = curr
            else:
                buffer2.next = head
                buffer2 = buffer2.next
                head.next = None
                head = curr
        
        if b1.next == None:
            return b2.next
        else:
            headhead = temp = b1.next
            b1.next = None
            while temp.next:
                temp = temp.next
        
        new_start = b2.next
        temp.next = new_start
        b2.next = None
        return headhead