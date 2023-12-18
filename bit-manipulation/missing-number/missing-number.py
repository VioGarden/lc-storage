# XOR order does not matter
# XOR - (2^3)
# 1 0 <-- 2
# 1 1 <-- 3
# 0 1 <-- answer

# XOR - 5 ^ 3 ^ 3
# 1 0 1 <-- 5
# 0 1 1 <-- 3
# 1 0 1 <-- 5 
# 0 1 1 <-- answer(3)

def missingNumber(nums):
    """for O(1) Memory"""
    

