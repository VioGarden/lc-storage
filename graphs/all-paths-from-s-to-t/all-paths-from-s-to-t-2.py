def allPathsSourceTarget(graph):
    final = []
    def dfs(path):
        print(path, "path")
        if path[-1] == len(graph)-1:
            print("added")
            final.append(path)
        else:
            print(graph[path[-1]], "graph[path[-1]]")
            for child in graph[path[-1]]:
                print(child, "child")
                dfs(path + [child])
    dfs([0])
    return final

# input: graph = [[1,2],[3],[3],[]]
# output: [[0,1,3],[0,2,3]]
# stdout: 
# [0] path
# [1, 2] graph[path[-1]]
# 1 child
# [0, 1] path
# [3] graph[path[-1]]
# 3 child
# [0, 1, 3] path
# added
# 2 child
# [0, 2] path
# [3] graph[path[-1]]
# 3 child
# [0, 2, 3] path
# added