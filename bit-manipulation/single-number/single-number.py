def singleNumber(nums):
    result = 0
    for n in nums:
        result = result ^ n
    return result

# one number in array nums has no duplicate, find the duplicate
