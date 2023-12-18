# Definition for singly-linked list.
# O(1) memory
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        # [1,2,2s,1]
        # [1,2,3s,2,1]
        slow, fast = head, head
        while fast and fast.next: # get middle
            slow = slow.next
            fast = fast.next.next
        prev = None

        while slow: # reverse list starting from slow
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev: # compare
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
            