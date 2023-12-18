
def canFinish(numCourses, prerequisites):

    graph = { i:[] for i in range(numCourses)}

    for course, prereq in prerequisites:
        graph[course].append(prereq)

    visit = set()

    def dfs(c):
        if c in visit:
            return False
        if graph[c] == []:
            return True
        
        visit.add(c)
        for elem in graph[c]:
            if not dfs(elem):
                return False
        visit.remove(c)
        return True

    for item in range(numCourses):
        if not dfs(item):
            return False
    return True