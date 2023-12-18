def canCross(stones):
    stone_set = set(stones)
    visited = set()
    def helper(position, jump_distance):
        # position, jump_distance (been there b4)
        # position + jump_distance not valid
        if (position + jump_distance) not in stone_set or (position, jump_distance) in visited:
            return False

        if position + jump_distance == stones[-1]:
            return True

        visited.add((position, jump_distance))
        return (helper(position + jump_distance, jump_distance - 1) or 
            helper(position + jump_distance, jump_distance + 1) or 
            helper(position + jump_distance, jump_distance))
    

    return helper(stones[0], 1)