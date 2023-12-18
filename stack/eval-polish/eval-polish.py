def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i == "+": 
            stack.append(stack.pop() + stack.pop()) # order doesn't matter when adding
        elif i == "-":
            first, second = stack.pop(), stack.pop() # lower in stack - stack top
            stack.append(second - first)
        elif i == "*":
            stack.append(stack.pop() * stack.pop()) # order doesn't matter when multiplying
        elif i == "/":
            first, second = stack.pop(), stack.pop() # lower in stack / stack top
            stack.append(int(second / first))
        else:
            stack.append(int(i)) # append as an int so operations possible
            
    return stack[0]


# evalRPN(["2","1","-","3","/"])