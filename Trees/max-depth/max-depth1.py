# use stack

class Solution(object):
    def maxDepth(self, root):

        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node: # ignores null nodes
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res

# maxDepth([3,9,20,null,null,15,7])

# iterative dfs