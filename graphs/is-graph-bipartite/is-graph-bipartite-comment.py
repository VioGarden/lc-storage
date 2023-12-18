class Solution:
    def isBipartite(self, graph):
        n = len(graph)    # Get the number of nodes in the graph
        colors = [0] * n    # Create a list to store the color assigned to each node

        for i in range(n):
            if colors[i] == 0:    # If the current node is not assigned a color
                if not self.helper(graph, colors, i, 1):    # Call the helper function to assign colors and check for bipartiteness
                    return False    # If the graph is not bipartite, return False
        return True    # If all nodes are assigned colors and the graph is bipartite, return True

    def helper(self, graph, colors, node, color):
        if colors[node] != 0:    # If the current node is already assigned a color
            return colors[node] == color    # Check if the assigned color matches the expected color
        
        colors[node] = color    # Assign the color to the current node

        for neighbor in graph[node]:    # Iterate through the neighbors of the current node
            if not self.helper(graph, colors, neighbor, -color):    # Recursively call the helper function for each neighbor with the opposite color
                return False    # If any neighbor is not assigned a valid color, return False
        
        return True    # If all neighbors are assigned valid colors, the graph is bipartite, so return True
