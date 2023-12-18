# deep copy (clone in different memory, new)
# will want to use a hashmap, and either dfs or bfs



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        otn = {} # hashmap
        def dfs(node):
            if node in otn: # already in hashmap, already clone made
                return otn[node] # return the clone, no need to create clone

            # clone does not exist
            copy = Node(node.val) # Node constructor
            otn[node] = copy # copy added to hashmap
            for nei in node.neighbors: # copy of every neighbor
                copy.neighbors.append(dfs(nei)) # all neightbors are set here
            return copy # return the copy mad ein current fn call
        return dfs(node) if node else None # call dfs and return result (any node returns, but doesnt matter)
        