# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    """"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        good, bad = 0, n
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid):
                bad = mid
                right = mid - 1
            else:
                good = mid
                left = mid + 1
        if isBadVersion(bad - 1):
            return bad - 1
        return bad