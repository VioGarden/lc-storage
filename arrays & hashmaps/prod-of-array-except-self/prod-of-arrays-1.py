def productExceptSelf(nums):
    result = [1] * (len(nums))              #array of 1's the length of nums (output array)
    
    pref = 1                                #prefix of 1
    for i in range(len(nums)):              #loop over array
        result[i] *= pref                   #multiply element by prefix
        pref *= nums[i]                     #increment prefix, multiply pref by nums[i]
        
    post = 1                                #postfix of 1
    for i in range(len(nums)-1, -1, -1):    #loop over array backwards
        result[i] *= post                   #multiply element by postfix
        post *= nums[i]                     #increment postfix 
        
    return result                           #return result array, multiply post by nums[i]

print(productExceptSelf([1,2,3,4]))
# output : [24,12,8,6]