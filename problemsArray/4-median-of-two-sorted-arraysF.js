/*
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
 var findMedianSortedArrays = function(nums1, nums2) {
    let nums3 = [...nums1]
    for(let i = 0; i < nums2.length; i++){
        nums3.push(nums2[i])
    }
    nums3.sort(function(a, b){return a - b})
    if(nums3.length%2===1){
        return nums3[Math.floor(nums3.length/2)];
    }
    else
        return (nums3[nums3.length/2] + nums3[nums3.length/2-1])/2
    
};
console.log(findMedianSortedArrays([1,2], [3,4]))
/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

*/