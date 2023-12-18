from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(root):
        q = deque()
        q.append(root)
        hashmap = {}
        while q:
            for i in range(len(q)):
                x = q.popleft()
                hashmap[x.val] = 1 + hashmap.get(x.val, 0)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        
        highest = max(hashmap.values())
        final = []
        for i in hashmap:
            if hashmap[i] == highest:
                final.append(i)
                
        return final
                
                