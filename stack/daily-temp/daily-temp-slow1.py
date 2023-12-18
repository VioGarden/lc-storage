
def dailyTemperatures(temperatures):
    output = [0]*len(temperatures) # output arrya of all 0
    stack = [] # empty stack
    for i, v in enumerate(temperatures): # index value
        if not stack: # if stack is empty
            stack.append([v, i]) # append value index
            continue
        if v < stack[-1][0]: # if current value is lesser than top of stack
            stack.append([v,i]) # append to stack
            continue # coninute needed to not do repeat calculations
        while stack and v > stack[-1][0]: # if stack exists and new value is greater
            diff = i - stack[-1][1] # difference is current to old
            output[stack[-1][1]] = diff # output index set to diff
            stack.pop() # pop top and repeat if scenario continues
        stack.append([v, i]) # append after while loop done
    return output # return output array