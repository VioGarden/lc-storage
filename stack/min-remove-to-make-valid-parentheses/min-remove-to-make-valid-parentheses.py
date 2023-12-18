def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    """
    open_parentheses = 0
    stack = list(s)

    for index, value in enumerate(stack):
        if stack[index] == '(':
            open_parentheses += 1
        if stack[index] == ')':
            if not open_parentheses:
                stack[index] = ''
            else:
                open_parentheses -= 1

    for i in range(len(stack) - 1, -1, -1):
        if not open_parentheses:
            break
        if stack[i] == '(':
            stack[i] = ''
            open_parentheses -= 1

    return ''.join(stack)
