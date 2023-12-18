def isValid(s):
    stack = []
    brack = {"]":"[", ")":"(", "}":"{"}

    for i in s:
        # if i isn't a closing parentheses
        if i not in brack:
            # append opening parentheses to stack
            stack.append(i)
            continue
        else:
            # if the stack is empty, or the top does not equal a counterpart of the closing parentheses
            if not stack or stack[-1] != brack[i]:
                # return false
                return False
            # if all good, pop the top
            stack.pop()
    # if stack is empty, returns true, else false
    return not stack