# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        while len(lists) > 1:
            ml = []
            for i in range(0, len(lists), 2):
                ll1 = lists[i]
                ll2 = lists[i + 1] if (i + 1) < len(lists) else None
                final = self.mergeList(ll1, ll2)
                ml.append(final)
            lists = ml
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next