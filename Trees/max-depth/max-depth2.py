# bfs search (level order traversal)
# use queue (root, replace with children, replace with children, when no more children, find level)
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0 
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

# iterative bfs