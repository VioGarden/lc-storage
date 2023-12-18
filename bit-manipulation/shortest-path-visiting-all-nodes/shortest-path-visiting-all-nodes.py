from collections import deque

# takeaways
# big memory bank
# bfs search (can repeat nodes)
# bit_mask tracker, 1111111 ending scenario

def shortestPathLength(graph):

    n = len(graph) # length of graph

    # node, bit mask (queue for bfs) (0, 1), (1,2), (2,4), (3,8) (essentially x, 2**x for x in range(n))
    queue_of_current_level = deque([(node, 1 << node) for node in range(n)])  # (node, bit_mask number)

    # bfs complete when bit_mask looks something like [1,1,1,1,1,1,1,1]
    final_bit_mask_destination = (1 << n) - 1

    # bit visited memory bank, 2**n by n
    visited = [[False for bit_mask in range(final_bit_mask_destination + 1)] for _ in range(n)]

    # set initial bit_mask locations to True
    for set_to_true in range(n):
        visited[set_to_true][1 << set_to_true] = True

    # keep track of answers
    path_length = 0
    
    while queue_of_current_level:

        curr_length = len(queue_of_current_level)

        while curr_length:

            node_to_check, curr_bit_mask = queue_of_current_level.popleft()

            # if you popped the ending bit_mask, you win
            if curr_bit_mask == final_bit_mask_destination:
                return path_length

            # bfs the graph
            for elem in graph[node_to_check]:

                # bitwise or, eventually leading to 11111111 scenario if possible
                new_bit_mask = curr_bit_mask | (1 << elem)

                if new_bit_mask == final_bit_mask_destination:
                    return path_length + 1
                
                # if node already visitied, don't need to expand from there
                if visited[elem][new_bit_mask]:
                    continue

                # append to queue, node to check from, and possible increase bit mask
                queue_of_current_level.append((elem, new_bit_mask))
                # visited section = True
                visited[elem][new_bit_mask] = True
            
            curr_length -= 1

        # update path size (aka our answer)
        path_length += 1
    
    return -1



