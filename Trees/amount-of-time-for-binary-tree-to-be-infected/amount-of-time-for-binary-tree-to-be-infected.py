from collections import defaultdict, deque

def amountOfTime(root, start):
    """
    :type root: Optional[TreeNode]
    :type start: int
    :rtype: int
    """
    graph = defaultdict(list)

    def build_adj(parent, small):
        if not small:
            return
        if parent:
            graph[parent.val].append(small.val)
            graph[small.val].append(parent.val)
        build_adj(small, small.left)
        build_adj(small, small.right)
    
    build_adj(None, root)


    visited = set()
    q = deque()
    q.append([start, 0])
    ans = 0
    while q:
        curr, level = q.popleft()
        visited.add(curr)
        ans = max(ans, level)
        for elem in graph[curr]:
            if elem not in visited:
                q.append([elem, level + 1])
    return ans