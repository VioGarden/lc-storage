def canFinish(numCourses, prerequisites):

    graph = [[] for _ in range(numCourses)]
    visit = [None for _ in range(numCourses)]

    for course, prereq in prerequisites:
        graph[course].append(prereq)

    def dfs(e):
        if visit[e] == False:
            return False
        
        if visit[e] == True:
            return True

        visit[e] = False
        for elem in graph[e]:
            if not dfs(elem):
                return False
        visit[e] = True
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True