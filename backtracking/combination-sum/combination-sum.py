def combinationSum(candidates, target):
    final = []
    def dfs(i, cur, tot):
        if tot == target: # if goal achieved, append copy to final
            final.append(cur[:])
            return
        if tot > target or i >= len(candidates): # overshoot target/finish iterations
            return

        dfs(i + 1, cur, tot) # next i in candidates

        cur.append(candidates[i]) # append same i to list
        dfs(i, cur, tot + candidates[i]) # same i, (cause duplicates allowed)
        cur.pop() # backtracking

    dfs(0, [], 0)
    return final

