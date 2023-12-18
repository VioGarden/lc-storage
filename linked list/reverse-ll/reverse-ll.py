# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head: # base case, if head null
            return None

        newHead = head # maintain new head, initially set to original head
        # if statement below only executes if size of list is greater than 1
        if head.next: # if we can keep reversing (linked lisrt extends), we call recursively
            newHead = self.reverseList(head.next) # call reverse, if returns something, set to new head
            head.next.next = head # reverses link
        head.next = None # if head is first in linked list, set next to null
        return newHead # returns new head

# recursively
# Time : O(n)
# Memory : O(n)
# Memory is O(n) because for every element, recursive call +1

# break down into sub problems (reverse remainder of linked list)
# head chanages (gets smaller linked list) till base case

# at base case, set next pointer to null

# at case 2, have access to two nodes
# next pointer of end, is set to second element (reversed)
# next pointer of second element is set to null

# last call, have access to three nodes
# second next pointer to new element (viewable by recursion)
# new elment next pointer to null

# since recursively, code must maintain last element as new head
