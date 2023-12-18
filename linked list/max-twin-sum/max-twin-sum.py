
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        array = [head.val]
        while head.next:
            head = head.next
            array.append(head.val)
        start, end = 0, len(array) - 1
        highest = array[start] + array[end]
        while start < end:
            start += 1
            end -= 1
            highest = max(highest, array[start] + array[end])
        return highest