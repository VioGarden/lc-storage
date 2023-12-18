class Solution(object):
    def maxVowels(self, s, k):
        vowel_set = {"a", "e", "i", "o", "u"}
        vowel_count = 0
        max_vowel_count = 0
        for i in range(k):
            if s[i] in vowel_set:
                vowel_count += 1
            max_vowel_count = max(max_vowel_count, vowel_count)
        for j in range(k, len(s)):
            remove_index = j - k
            add_index = j

            if s[remove_index] in vowel_set:
                vowel_count -= 1
            if s[add_index] in vowel_set:
                vowel_count += 1

            if vowel_count == k:
                return k

            max_vowel_count = max(max_vowel_count, vowel_count)
        
        return max_vowel_count