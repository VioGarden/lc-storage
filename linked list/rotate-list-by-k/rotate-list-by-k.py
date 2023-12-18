# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        # finding length
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        change = k%length # how many iterations to do

        if change == 0: # if change is 0, no change to list
            return head

        iterate_from_start = length - change 

        turning_point = head
        while iterate_from_start > 1: # its > 1 and not > 0 because want to prev Node
            turning_point = turning_point.next
            iterate_from_start -= 1
        
        begin_point = turning_point.next # new start of new list
        turning_point.next = None

        new_start = begin_point

        while begin_point.next:
            begin_point = begin_point.next

        begin_point.next = head

        return new_start

        


