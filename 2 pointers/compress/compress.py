def compress(chars):
    left, right = 0, 0
    while right < len(chars):
        chars[left] = chars[right]
        count = 1
        while right < len(chars) - 1 and chars[right] == chars[right + 1]:
            right += 1
            count += 1
        
        if count > 1:
            for c in str(count):
                chars[left + 1] = c
                left += 1
        left += 1
        right += 1
    return left 