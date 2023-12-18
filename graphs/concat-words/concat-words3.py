class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        s = set(words)
        final = []
        for w in words:
            if self.dfs(w, s):
                final.append(w)
        return final
        

    def dfs(self, word, s):
        for i in range(1, len(word)):
            pref = word[:i]
            suff = word[i:]
            if pref in s and (suff in s or self.dfs(suff, s)):
                return True
        return False

