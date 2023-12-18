//Third method using Set() (Fastest runtime at 91.95% and very readable code)
var containsDuplicate = function (nums) {
    //Pass the array into a Set() (which removes duplicates) and then compare its size to the original array.
    return new Set(nums).size !== nums.length;
};