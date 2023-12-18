def containsDuplicate(nums):
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
        else:
            return True
    return False

#runtime 5%
#memory 89%