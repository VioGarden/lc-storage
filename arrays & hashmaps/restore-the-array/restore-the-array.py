from collections import defaultdict

def restoreArray(adjacentPairs):
    """
    :type adjacentPairs: List[List[int]]
    :rtype: List[int]
    """
    hashmap = defaultdict(list)
    for x, y in adjacentPairs:
        hashmap[x].append(y)
        hashmap[y].append(x)
    table = hashmap.items()
    for key, value in table:
        if len(value) == 1:
            prev = key
            curr = value[0]
            break
    arr = []
    for _ in range(len(table) - 2):
        arr.append(prev)
        two_values = hashmap[curr]
        if two_values[0] == prev:
            prev = curr
            curr = two_values[1]
        else:
            prev = curr
            curr = two_values[0]
    arr.extend((prev, curr))
    return arr

"""Other methods after creating adjacency list"""
"""popping"""
    # arr = [key]
    # while hashmap[node]:
        
    #     # get the next element
    #     # (there can only be one, as we always remove one)
    #     new = hashmap[node].pop()
        
    #     # append the new element to the list
    #     arr.append(new)
        
    #     # delete node from the next connections
    #     hashmap[new].remove(node)
        
    #     # set the new element
    #     node = new
    # return arr
"""dfs"""
    # arr=[]
    # seen = set()
    # def dfs(num):
    #     seen.add(num)
    #     for next_num in hashmap[num]:
    #         if next_num in seen: continue
    #         dfs(next_num)
    #     arr.append(num) 
    # dfs(key)
    # return arr