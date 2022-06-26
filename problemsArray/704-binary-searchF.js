/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    while(left <= right){
        let pivot = left + Math.floor((right - left)/2);
        if (nums[pivot] === target) return pivot
        if(target < nums[pivot]) right = pivot - 1
        else if(target > nums[pivot]) left = pivot + 1
        if (left > right && nums[left] !== target) return [-1] 
    }
};
console.log(search([-1,0,3,5,9,12],2))