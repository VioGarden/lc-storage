from collections import defaultdict

def maximumDetonation(self, bombs):
    n, ans, final = len(bombs), 0, defaultdict(list)

    for i in range(n):
        for j in range(n):
            if i == j: continue
            if bombs[i][2]**2 >= (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2:
                final[i] += [j]
    
    def dfs(node, visited):
        for child in final[node]:
            if child not in visited:
                visited.add(child)
                dfs(child, visited)
    
    for i in range(n):
        visited = set([i])
        dfs(i, visited)
        ans = max(ans, len(visited))
    
    return ans