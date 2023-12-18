def removeKdigits(num, k):
    stack = []
    for n in num:
        while stack and k and stack[-1] > n:
            stack.pop()
            k -= 1
        if stack or n != '0':
            stack.append(n)
    if k:
        stack = stack[0:-k]
    return "".join(stack) or "0"


num = "1432219"
k = 3

removeKdigits(num, k)