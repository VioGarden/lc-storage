def findAllConcatenatedWordsInADict(words):
    s = set(words)
    def dfs(word):
        for i in range(len(word)):
            pref = word[:i]
            suff = word[i:]
            if pref in s and suff in s:
                return True
            if pref in s and dfs(suff):
                return True
            if suff in s and dfs(pref):
                return True
        return False
    final = []
    for i in words:
        if dfs(i):
            final.append(i)
    return final

words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(findAllConcatenatedWordsInADict(words))
