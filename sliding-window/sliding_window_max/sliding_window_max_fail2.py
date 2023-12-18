# works but slow

def maxSlidingWindow(nums, k):

    output = []

    def findvals(start, end):
        hold = [nums[start], start]
        for num in range(start, end):
            if nums[num] > hold[0]:
                hold[0] = nums[num]
                hold[1] = num
        return hold

    cya = findvals(0, k)
    output.append(cya[0])

    for i in range(k, len(nums)):
        curr_num = nums[i]
        curr_pos = i
        top_num = cya[0]
        top_pos = cya[1]
        if top_pos < (curr_pos - k + 1):
            cya = findvals(curr_pos - k + 1, curr_pos + 1)
            output.append(cya[0])
            cya[1] -= 1
        else:
            if curr_num > top_num:
                cya[0] = curr_num
                cya[1] = curr_pos
                output.append(cya[0])
                cya[1] -= 1
            else:
                output.append(top_num)
                cya[1] -= 1
    
    return output