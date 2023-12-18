def containsDuplicate(nums):
    hashset = set()
    for i in nums:
        if i not in hashset:
            hashset.add(i)
        else:
            return True
    return False