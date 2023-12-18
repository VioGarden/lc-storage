class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        colors = [0] * n

        for i in range(n):
            if colors[i] == 0:
                if not self.helper(graph, colors, i, 1):
                    return False
        return True
    
    def helper(self, graph, colors, node, color):
        if colors[node] != 0:
            return colors[node] == color
        
        colors[node] = color

        for neighbor in graph[node]:
            if not self.helper(graph, colors, neighbor, -color):
                return False
        
        return True