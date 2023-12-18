def decodeString(s):
    stack = []
    current = ""
    k = 0
    for char in s:
        if char == "[":
            stack.append((current, k))
            current = ""
            k = 0
        elif char == "]":
            first, second = stack.pop()
            current = first + second * current
        elif char.isdigit():
            k = k*10 + int(char)
        else:
            current += char
    return current

s = "2[abc]3[cd]ef"
decodeString(s) # abcabccdcdcdef"
