'use strict'
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var threeSumClosest = function(nums, target) {
    let sum = 0
    let min = 10001;
    let value;
    nums.sort(function(a, b){return a - b})
    for(let i = 0; i < nums.length - 2; i++){
        for(let j = i + 1; j < nums.length - 1; j++){
            let left = 0;
            let right = nums.length - 1;
            let k
            let target_sum = target - nums[i] - nums[j]
            while(left <= right){
                let pivot = left + Math.floor((right - left)/2);
                if(nums[pivot] === target_sum){
                    return target
                }
                if((target_sum < nums[pivot] && pivot - 1 !== i && pivot - 1 !== j)||pivot + 1 === i || pivot + 1 === j){
                    right = pivot - 1
                }
                else if((target_sum > nums[pivot] && pivot + 1 !== i && pivot + 1 !== j)||pivot - 1 === i || pivot - 1 === j){
                    left = pivot + 1
                }
            }
            if(nums[left] - target_sum > 0 &&((nums[left] - target_sum <= target_sum - nums[left - 1] || left === 0)|| (left - 1 === i || left -1 === j))&& left !== i && left !== j ){
                sum = nums[i] + nums[j] + nums[left];
                if(sum - target < min){
                    min = sum - target;
                    value = sum
                }
            } 
            else if(nums[left] - target_sum < 0&&((nums[left] - target_sum >= target_sum - nums[left-1]|| typeof nums[left] === 'undefined')|| (left === i || left === j)) && left - 1 !== i && left - 1 !== j){
                sum = nums[i] + nums[j] + nums[left - 1];
                if(target - sum < min){
                    min = target - sum
                    value = sum
                }
            }
        }
    }
    return value;
      
};
console.log(threeSumClosest([-1,2,1,-4], 1))
// console.log(threeSumClosest([1,1,-1,-1,3], 1))
// };
// console.log(threeSumClosest([0,1,2], 3));