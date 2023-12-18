class Solution:
    def partition(self, s):
        final = []
        part = []
        def backtrack(i):
            if i >= len(s):
                final.append(part[:])
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return final

    def isPalindrome(self, s, start, finish):
        while start < finish:
            if s[start] != s[finish]:
                return False
            start += 1
            finish -= 1
        return True 