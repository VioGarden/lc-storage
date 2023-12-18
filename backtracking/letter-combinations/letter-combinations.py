def letterCombinations(digits):
    if not digits:
        return []
    
    hashmap = {"2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",}
    
    final = []
    
    def backtrack(i, curstr):
        if len(curstr) == len(digits):
            final.append(curstr)
            return
        for j in hashmap[digits[i]]:
            backtrack(i + 1, curstr + j)
            
    backtrack(0, "")
    
    return final