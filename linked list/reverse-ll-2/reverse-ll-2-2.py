class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        prev, curr = ListNode(-1, head), head
        ans = prev
        for _ in range(1, left):
            prev, curr = prev.next, curr.next
        next_node = None
        for _ in range(left, right + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp
        prev.next.next = curr
        prev.next = next_node
        return ans.next
