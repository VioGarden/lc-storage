"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root: return None
        cur, nxt = root, root.left
        while cur and nxt:
            cur.left.next = cur.right # sets path between node
            if cur.next: # (5 --> 6) if there is a jump
                cur.right.next = cur.next.left # (2-->5.next) = (2-->3.left)
            cur = cur.next # every time, cur = cur.next
            if not cur: # when cur --> Null
                cur = nxt # 'nxt' was already set to next level down 
                nxt = cur.left # sets 'nxt' to next level down 
        return root