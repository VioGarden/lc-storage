def countHomogenous(self, s):
    """
    :type s: str
    :rtype: int
    """
    ans, left = 0, 0
    for right, char in enumerate(s):
        if char == s[left]:
            ans += right - left + 1
        else:
            left = right
            ans += 1
    return ans % 1000000007
    