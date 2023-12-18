class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            num = self.isSub(s, i)
            count += num
        return count
        
    def isSub(self, s, index):
        counter = 0
        left, right = index, index
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            counter += 1
        left, right = index, index + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            counter += 1
        return counter
    