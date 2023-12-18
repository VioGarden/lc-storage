from collections import deque


# bfs search
def allPathsSourceTarget(graph):
    final = [] # final
    q = deque([[0]])
    while q:
        path = q.popleft()
        if path[-1] == len(graph) - 1:
            final.append(path)
        else:
            q.extend(path + [child] for child in graph[path[-1]])
    return final