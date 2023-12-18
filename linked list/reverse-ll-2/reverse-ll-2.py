# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        temp_prev = dummy
        curr = head
        count = 1
        while count < left:
            temp_prev = curr
            curr = curr.next
            count += 1
        
        prev = None
        while count <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1

        temp_prev.next.next = curr
        temp_prev.next = prev
        return dummy.next