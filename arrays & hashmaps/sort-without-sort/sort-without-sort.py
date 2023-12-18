from collections import deque

class Solution(object):
    def sortArray(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            front, end = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])
            nums = self.help(front, end)
        return nums
    def help(self, a, b):
        result = []
        aa = deque(a)
        bb = deque(b)
        while aa and bb:
            if aa[0] <= bb[0]:
                result.append(aa.popleft())
            else:
                result.append(bb.popleft())
        result.extend(aa or bb)
        return result
