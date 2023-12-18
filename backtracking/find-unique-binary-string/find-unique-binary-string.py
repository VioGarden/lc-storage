def findDifferentBinaryString(nums):
    """
    :type nums: List[str]
    :rtype: str
    """
    ans = ""
    for i in range(len(nums)):
        current_char = nums[i][i]
        oppo_char = '1' if current_char == '0' else '0'
        ans += oppo_char
    return ans