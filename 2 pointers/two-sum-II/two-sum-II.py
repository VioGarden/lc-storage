def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1  # initialize pointers
    # while target is not met, loop over
    while numbers[left] + numbers[right] != target: 
        value = numbers[left] + numbers[right] # easier as a variable
        if value == target: # if value is target, return
            return [left+1, right+1]
        elif value > target: # if value overshoots
            right -= 1  # decrement right variable
        else: # if value undershoots
            left += 1  # increment left variable
    return [left+1, right+1]  # return index + 1

print(twoSum([2,7,11,15], 9))
# output : True
