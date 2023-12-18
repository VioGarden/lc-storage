def generateParentheses(n):
    # only add open parenthesis if open < n
    # only add closing parenthesis if closed < open
    # valid IF open == closed == n

    # do it recusively and stack

    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n: # base case, stack contains proper parentheses
            res.append("".join(stack)) # every char in stack, join into empty string, append to result list
            return
        
        if openN < n: # open count less than end
            stack.append("(")
            backtrack(openN + 1, closedN) # continue backtrack (recursively calling (creates recursion))
            stack.pop() # update stack, single stack variable, stack is global, opo recently added

        if closedN < openN:
            stack.append(")") # append (")")
            backtrack(openN, closedN + 1) # continue backtrack
            stack.pop() 

    backtrack(0,0)
    return res