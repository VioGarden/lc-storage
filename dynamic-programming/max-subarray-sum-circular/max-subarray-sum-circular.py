def maxSubarraySumCircular(nums):

    def maxSubarray(nums):
        if not nums:
            return 0
        curr = total = nums[0]
        for i in nums[1:]:
            curr = max(curr + i, i)
            total = max(total, curr)
        return total

    def minSubarray(nums): # the first element and the last element are exclusive!
        if len(nums) <= 2:
            return 0
        curr = total = nums[0]
        for i in nums[1:len(nums) - 1]:
            curr = min(curr + i, i)
            total = min(total, curr)
        return total

    # def minimumSubarray(nums):  # the first element and the last element are exclusive!
    #     if len(nums) <= 2: return 0
    #     ans = nums[1]
    #     sumSoFar = 0
    #     for i in range(1, len(nums) - 1):
    #         sumSoFar += nums[i]
    #         ans = min(ans, sumSoFar)
    #         if sumSoFar > 0:
    #             sumSoFar = 0
    #     return ans

    return max(maxSubarray(nums), sum(nums) - minSubarray(nums))