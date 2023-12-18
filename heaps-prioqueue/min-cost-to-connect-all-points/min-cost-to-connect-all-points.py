from collections import heapq

def minCostConnectPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    n = len(points)
    adj = { i:[] for i in range(n) }
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])
    
    ans = 0
    min_heap = [[0, 0]] # cost, adj
    visited = set()
    
    while len(visited) < n:
        curr_count, i = heapq.heappop(min_heap)
        if i in visited:
            continue
        visited.add(i)
        ans += curr_count
        for neighbor_count, neighbor in adj[i]:
            if neighbor not in visited:
                heapq.heappush(min_heap, [neighbor_count, neighbor])
    return ans