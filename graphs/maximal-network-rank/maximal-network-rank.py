def maximalNetworkRank(n, roads):

    highest = 0

    connections = { i:set() for i in range(n) }

    for i, j in roads:
        connections[i].add(j)
        connections[j].add(i)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            highest = max(highest, len(connections[i]) + len(connections[j]) - (j in connections[i]))
        
    return highest