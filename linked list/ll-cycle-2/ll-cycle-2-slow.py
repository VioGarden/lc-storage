# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(head):
        if not head:
            return None
        visit = set()
        slow = head
        while slow.next:
            if slow in visit:
                return slow
            visit.add(slow)
            slow = slow.next
            
        return None