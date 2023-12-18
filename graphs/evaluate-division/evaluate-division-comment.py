from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        
        # Build the adjacency list representation of the graph
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])    # Add directed edge from 'a' to 'b' with the given value
            adj[b].append([a, 1 / values[i]])    # Add directed edge from 'b' to 'a' with the reciprocal value
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1    # If either source or target node is not present in the graph, return -1
                
            q, visit = deque(), set()
            q.append([src, 1])    # Start BFS from the source node with an initial weight of 1
            visit.add(src)
            
            while q:
                n, w = q.popleft()    # Dequeue the next node and its accumulated weight
                if n == target:
                    return w    # If the target node is reached, return the accumulated weight
                
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])    # Enqueue unvisited neighbor nodes with updated weight
                        visit.add(nei)    # Mark the neighbor node as visited
            
            return -1    # If the target node is not reached, return -1
        
        # Perform BFS for each query and collect the results
        return [bfs(q[0], q[1]) for q in queries]
