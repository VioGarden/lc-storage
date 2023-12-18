def closestMeetingNode(edges, node1, node2):
    
    def dfs(node, edges, distance, visited):
        """
        given a starting node, 
        finds the nodes that connect from the starting node and tracks distance
        """
        visited[node] = True
        neighbor = edges[node]
        if neighbor != -1 and visited[neighbor] == False:
            distance[neighbor] = distance[node] + 1
            dfs(neighbor, edges, distance, visited)        

    # creating useful arrays
    n = len(edges)
    dist1, dist2, vis1, vis2 = [0]*n, [0]*n, [False]*n, [False]*n
    ans = -1
    min_distance = float("inf")
    dfs(node1, edges, dist1, vis1)
    dfs(node2, edges, dist2, vis2)

    for curr in range(n):
        # iterates over each index, trying to find min_distance
        if vis1[curr] and vis2[curr] and min_distance > max(dist1[curr], dist2[curr]):
            min_distance = max(dist1[curr], dist2[curr])
            ans = curr
    return ans


edges = [2,2,3,-1]
node1 = 0
node2 = 1
print(closestMeetingNode(edges, node1, node2))
    