# swapping values
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNode(self, head, k):
        dummy = pre_left = pre_right = ListNode(next=head)
        right = left = head
        for i in range(k - 1):
            pre_left = left
            left = left.next
        
        null_checker = left
        while null_checker.next:
            pre_right = right
            right = right.next
            null_checker = null_checker.next
        
        if left == right:
            return head
        
        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next