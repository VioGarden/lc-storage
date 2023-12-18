class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        theDeepest = [0]
        
        def dfs(node, depth):
            if node.left or node.right:
                if node.left: dfs(node.left, depth + 1)
                if node.right: dfs(node.right, depth + 1)
            else:
                if depth > theDeepest[0]:
                    theDeepest[0] = depth
                    
        dfs(root, 1)
        
        return theDeepest[0]
    