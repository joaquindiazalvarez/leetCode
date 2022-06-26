/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 var threeSum = function(nums) {
    let triplets = []
    let zerotriplet = false
    nums.sort(function(a, b){return a - b})
    for(let i = 0; i < nums.length - 1; i++){
        for(let j = i + 1; j < nums.length - 1; j++){
            let target = -(nums[i]+nums[j]);
            let left = 0;
            let right = nums.length - 1;
            let k;
            while(left<=right){
                let pivot = left + Math.floor((right - left)/2);
                if (nums[pivot] === target && pivot !== i && pivot !== j){
                    k = pivot
                    let triplet = [nums[i], nums[j], nums[k]]
                    if(!(triplets.some(c => {return (c.includes(nums[i]) && c.includes(nums[j]) && c.includes(nums[k]))}))&&(nums[i]!==0&&nums[j]!==0&&nums[k]!==0)){
                        triplets.push(triplet);
                    }
                    else if((nums[i]===0&&nums[j]===0&&nums[k]===0) && zerotriplet === false){
                        triplets.push(triplet)
                        zerotriplet = true
                    } 
                }
                if(target < nums[pivot]){
                    right = pivot - 1
                }
                else{
                    left = pivot + 1
                }
            }
            /* for(let k = j + 1; k < nums.length; k++){
                let triplet = [nums[i], nums[j], nums[k]]
                console.log(triplet)
                if(nums[i] + nums[j] + nums[k] === 0 && !(triplets.some(c => {return c[0]===nums[i] && c[1]===nums[j] && c[2]===nums[k]}))){
                    triplets.push(triplet);
                }
            
            } */
        }
    }   
    return triplets;
    
};
console.log(threeSum([0, 0, 0, 0]))
/* 
console.log(threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])); 
[ [ -5, 1, 4 ],
  [ -4, 0, 4 ],
  [ -4, 1, 3 ],
  [ -2, -2, 4 ],
  [ -2, 1, 1 ],
  [ 0, 0, 0 ] ]
*/