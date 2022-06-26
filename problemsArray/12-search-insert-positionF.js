/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while(right >= left){
        let pivot = left + Math.floor((right - left)/2);
        if(nums[pivot] === target){
            return pivot
        }
        if(nums[pivot] > target){
            right = pivot - 1
        }
        else if(nums[pivot] < target){
            left = pivot + 1
        }
    }
    return left
};
console.log(searchInsert([1,3,5,6,7,8,9,10],5))