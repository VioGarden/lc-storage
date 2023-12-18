def minSwaps(s):
    # find number of unbalned (filter out balanced)
    # from there, can calculate how many swaps
    # 1,2 --> 1
    # 3,4 --> 2
    stack = []
    for i in s:
        if i == "[":
            stack.append(i)
        else:
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
    bad_brackets_with_matches = len(stack) # will be even
    bad_brackets_total = bad_brackets_with_matches//2
    num_swaps = -(-bad_brackets_total//2)
    return num_swaps

s = "]]][[["
print(minSwaps(s))