# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head # previous is null/None, current is head
        while curr: # while current is not None/null
            nxt = curr.next # temp var to hold next to move pointer up
            curr.next = prev # reversing linked list
            prev = curr # prev pointer moved to curr
            curr = nxt # curr pointer moved to nxt
        return prev # prev is the head!!! (of the reversed linked list)


# iteratively
# Time : O(n)
# Memory : O(1)

# two pointers
# current pointer : initialize to head/first node
# previous pointer : initialize to Null

# first node, reverse next pointer (becomes last element) (points to null)
# prev pointer shifted to current
# current pointer shifted to next node

# current next pointer reversed
# prev pointer shifted to current
# current pointer shifted to next node

# repeat

# (end case)
# current next pointer revesed 
# prev pointer to current (final node) (**the new head**)
# current pointer shifted to null (forget this pointer)
