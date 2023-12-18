//Second method using Map() (Has to map entire array but code is more readable)
var containsDuplicate = function (nums) {
    //create a new hashmap with all the items in the array. Any duplicates will be removed.
    const totalWithoutDuplicates = new Map(nums.map((i) => [i]));

    //check if the size of the initial array is larger than the new hashmap.
    return totalWithoutDuplicates.size !== nums.length;
};