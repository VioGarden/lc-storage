
def permute(nums):
    def rec(num, curr=[], end=[]):
        if not num:
            end.append(curr[:])
        
        for i in range(len(num)):
            x = num[:i] + num[i + 1:]
            curr.append(nums[i])
            rec(x, curr, end)
            curr.pop()
            
        return end
    return rec(nums)


x = [2,4,5]

print(permute(x))
