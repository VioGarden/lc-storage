def maxLengthBetweenEqualCharacters(s):
    """
    :type s: str
    :rtype: int
    """
    hashmap, ans = {}, -1
    for index, character in enumerate(s):
        if character not in hashmap:
            hashmap[character] = index
        else:
            ans = max(ans, index - hashmap[character] - 1)
    return ans
