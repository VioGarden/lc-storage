
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        hashmap = {}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                hashmap[curr].next = hashmap[curr.next]
            if curr.random:
                hashmap[curr].random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]