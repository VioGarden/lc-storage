def reorderList(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow.next, prev, curr = None, None, slow.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    left, right = head, prev
    while right:
        temp1, temp2 = left.next, right.next
        left.next = right
        right.next = temp1
        left, right = temp1, temp2