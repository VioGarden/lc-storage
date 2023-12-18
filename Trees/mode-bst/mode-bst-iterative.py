class Solution:
    """
    iterative dfs
    """
    def findMode(self, root):
        pre, max_count, curr_count, res = None, 0, 0, []
        if not root:
            return
        stack = []
        while True:
            while root:
                stack.append(root)            
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            curr_count = 1 if node.val != pre else curr_count + 1
            if curr_count == max_count:
                res.append(node.val)
            elif curr_count > max_count:
                res = [node.val]
                max_count = curr_count 
            pre = node.val
            root = node.right