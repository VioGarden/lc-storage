from collections import deque

def ladderLength(beginWord, endWord, wordList):    

    if endWord not in set(wordList):
        return 0

    def compare(worda, wordb):
        stack = []
        for i in worda:
            stack.append(i)
        stack_a = deque(stack)

        mismatches = 0
        for i in range(len(stack_a)):
            temp_a = deque.popleft(stack_a)
            if temp_a != wordb[i]:
                mismatches += 1
            if mismatches > 1:
                break
        
        if mismatches == 1:
            return True
        return False


    word_map = {}
    if beginWord not in set(wordList):
        wordList.append(beginWord)
    if endWord not in set(wordList):
        wordList.append(endWord)
    print(wordList)
    end = len(wordList)
    for first in range(end):
        for second in range(first, end):
            word1, word2 = wordList[first], wordList[second]
            if compare(word1, word2):
                if word1 not in word_map:
                    word_map[word1] = []
                word_map[word1].append(word2)
                if word2 not in word_map:
                    word_map[word2] = []
                word_map[word2].append(word1)
    if not word_map or beginWord not in word_map:
        return 0
    print(word_map)

    visited = set()
    final = []
    def dfs(begin, end, deep):
        for i in word_map[begin]:
            if i == end:
                final.append(deep)
                print(final, deep)
            if (begin, i) not in visited:
                visited.add((begin, i))
                dfs(i, end, deep + 1)

    dfs(beginWord, endWord, -1)

    if not final:
        return 0
    return min(final)

        
# print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(ladderLength("hot", "dog",["hot","cog","dog","tot","hog","hop","pot","dot"]))
# ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])
# print(ladderLength("hot", "dog",["hot","dog"]))