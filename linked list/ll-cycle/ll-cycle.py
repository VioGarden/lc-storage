
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head # init to heads
        while fast and fast.next: # whlie next 2 exist and are not null
            slow = slow.next # increment slow
            fast = fast.next.next # double increment fast
            if slow == fast: # if equal, return True
                return True 
        return False