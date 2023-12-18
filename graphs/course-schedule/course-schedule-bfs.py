from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    # Initialize a dictionary to store courses and their prerequisites
    todo = {i: set() for i in range(numCourses)}
    
    # Initialize a defaultdict to store a graph of course dependencies
    graph = defaultdict(set)
    
    # Build the todo dictionary and graph from the prerequisites list
    for course, prereq in prerequisites:
        todo[course].add(prereq)
        graph[prereq].add(course)
        
    # Initialize a deque (double-ended queue) for BFS traversal
    q = deque([])
    
    # Populate the queue with courses that have no prerequisites
    for course_key, prereq_value in todo.items():
        if len(prereq_value) == 0:
            q.append(course_key)
    
    # Perform BFS traversal to find if all courses can be finished
    while q:
        # Get the next course in the queue
        curr = q.popleft()
        
        # Iterate through the courses that depend on the current course
        for i in graph[curr]:
            # Remove the current course from their prerequisites
            todo[i].remove(curr)
            
            # If a course has no more prerequisites, add it to the queue
            if len(todo[i]) == 0:
                q.append(i)
        
        # Remove the current course from the todo dictionary
        todo.pop(curr)
    
    # If there are no remaining courses in the todo dictionary,
    # then all courses were finished successfully
    return not todo
