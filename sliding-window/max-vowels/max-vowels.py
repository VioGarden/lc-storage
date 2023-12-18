class Solution(object):
    def maxVowels(self, s, k):
        vowel_set = {"a", "e", "i", "o", "u"}
        vowel_count = 0
        max_vowel_count = 0
        
        for index, count in enumerate(s):
            if count in vowel_set:
                vowel_count += 1
            if index >= k and s[index - k] in vowel_set:
                vowel_count -= 1
            max_vowel_count = max(vowel_count, max_vowel_count)
        
        return max_vowel_count