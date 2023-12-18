class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = r = i
            res += self.countPali(s, l, r)
            res += self.countPali(s, i, i + 1)

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            left -= 1
            right += 1
        return res