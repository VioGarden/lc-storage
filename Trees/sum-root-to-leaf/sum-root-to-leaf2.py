from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root):
        dq, final = deque(), 0
        dq.append([root, 0])

        while dq:
            rootroot, current = dq.popleft()
            if not rootroot.left and not rootroot.right:
                final += (current*10 + rootroot.val)
            if rootroot.right:
                dq.append([rootroot.right, current*10 + rootroot.val])
            if rootroot.left:
                dq.append([rootroot.left, current*10 + rootroot.val])
        return final