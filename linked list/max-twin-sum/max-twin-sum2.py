
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):

        slow, fast = head, head
        maxVal = 0

        # slow is mid of ll
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second part of ll
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # get max sum of pairs
        while prev:
            maxVal = max(maxVal, head.val + prev.val)
            prev = prev.next
            head = head.next
        
        return maxVal