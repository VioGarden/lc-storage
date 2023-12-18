def findAllConcatenatedWordsInADict(words):
    s = set(words)
    memo = {}
    def dfs(word):
        if word in memo:
            return memo[word]
        memo[word] = False
        for i in range(1, len(word)):
            pref = word[:i]
            suff = word[i:]
            if pref in s and suff in s:
                memo[word] = True
                break
            if pref in s and dfs(suff):
                memo[word] = True
                break
            if suff in s and dfs(pref):
                memo[word] = True
                break
        return memo[word]
    return [word for word in words if dfs(word)]
    
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
