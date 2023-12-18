from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        direction = 1
        final = []
        while q:
            remember = []
            for _ in range(len(q)):
                curr = q.popleft()
                remember.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            final.append(remember[::direction])
            direction *= -1
        return final