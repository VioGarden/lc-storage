var twoSum = function(nums, target) {
    const hashMap = {};
    for(let i = 0; i < nums.length; i++){
        let difference = target - nums[i]
        if(difference in hashMap){
            return [hashMap[difference],i]
        }
        hashMap[nums[i]] = i
    }
};