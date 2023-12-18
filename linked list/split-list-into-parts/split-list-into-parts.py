# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        ans = [[] for _ in range(k)]

        splits, remain = length // k, length % k # splits, remain = divmod(length, k)

        prev, curr = None, head

        for i in range(k):
            ans[i] = curr
            for _ in range(splits + (1 if remain > 0 else 0)):
                prev, curr = curr, curr.next
            if prev:
                prev.next = None
            remain -= 1
        return ans
                