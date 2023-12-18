# backtrcking time limit exceeded
def countGoodStrings(low, high, zero, one):

    mod = 10**9 + 7
    
    def helper(length):
        if length > high:
            return 0
        result = 1 if length >= low else 0
        result += helper(length + zero) + helper(length + one)
        return result % mod
    
    return helper(0)
