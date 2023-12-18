class Solution:
    def swapNodes(self, head, k):
        first = last = head
        for i in range(1, k):
            first = first.next
        
        null_checker = first
        while null_checker.next:
            last = last.next
            null_checker = null_checker.next
        first.val, last.val = last.val, first.val
        return head
