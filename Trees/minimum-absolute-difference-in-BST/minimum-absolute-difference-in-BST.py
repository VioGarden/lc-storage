def getMinimumDifference(root):
    arr = []
    def dfs(node):
        if node.left: 
            dfs(node.left)
        arr.append(node.val)
        if node.right:
            dfs(node.right)
    dfs(root)
    return min(b - a for a, b in zip(arr, arr[1:]))
