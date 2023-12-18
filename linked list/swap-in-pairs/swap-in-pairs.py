class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):

        if not head or not head.next:
            return head 

        prev = ListNode(0)
        curr = head.next

        while head and head.next:
            temp = head.next 
            head.next = temp.next 
            temp.next = head
            prev.next = temp
            head = head.next
            prev = temp.next 
        
        return curr