def minSwaps(s):
    # different way to count number of opened parenthesis
    opened = 0
    final = 0
    for i in s:
        if i == "[":
            opened -= 1
        elif i == "]":
            opened += 1
        
        final = max(final, opened)
        print(final)
            
    return (final+1)// 2