def productExceptSelf(nums):
    pref = 1                                #prefix initialized to 1
    prefix = [1] * len(nums)                #prefix array of 1's
    post = 1                                #postfix initialized to 1
    postfix = [1] * len(nums)               #postfix array of 1's
    output = []                             #output array initialized
    for i in range(len(nums)):              #loop over and create prefix array
        pref *= nums[i]                     #pref var changed
        prefix[i] *= pref                   #prefix array index changed        
        #[1, 2, 6, 24]

    for i in range(len(nums) - 1, -1,-1):   #loop over backwards and create postfix array
        post *= nums[i]                     #post var changed
        postfix[i] *= post                  #postix array index changed
        #[24,24,12,4]

    for i in range(len(nums)):              #iterate over length of nums
        if i == 0:                          #if beginning
            output.append(postfix[i + 1])   #append the postfix to the output array
        elif i == len(nums) - 1:            #if end
            output.append(prefix[i - 1])    #append the prefix to the output array
        else:                                           #else
            output.append(prefix[i-1] * postfix[i+1])   #append prefix * postfix to output array

    return output                           #return output array


print(productExceptSelf([1,2,3,4]))
# output : [24,12,8,6]