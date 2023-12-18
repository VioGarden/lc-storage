def dailyTemperatures(temperatures):
    output = [0]*len(temperatures)
    stack = []
    for i, v in enumerate(temperatures):
        while stack and v > stack[-1][0]:
            vt, it = stack.pop()
            output[it] = i - it
        stack.append([v, i])
    return output