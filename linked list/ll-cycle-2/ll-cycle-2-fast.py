# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):   
        if not head or not head.next:
            return None
            
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        if slow != fast:
            return None
        
        while head != slow:
            head = head.next
            slow = slow.next
            
        return slow