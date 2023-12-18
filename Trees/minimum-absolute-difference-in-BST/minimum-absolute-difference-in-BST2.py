def getMinimumDifference(root):
    prev = float("-inf")
    min_diff = float("inf")

    def dfs(root):
        nonlocal prev, min_diff
        if not root:
            return
        
        if root.left:
            dfs(root.left)
        
        if (root.val - prev) < min_diff:
            min_diff = root.val - prev
        
        prev = root.val

        if root.right:
            dfs(root.right)
    
    dfs(root)
    return min_diff