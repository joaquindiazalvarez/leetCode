from typing import List
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        valid = True
        length = len(arr)
        breakindex = length
        if length >= 3 and arr[0] < arr[1] and arr[-1] < arr[-2]:
            for i in range(1, length):
                if arr[i] < arr[i - 1]:
                    breakindex = i
                    break
                if arr[i] == arr[i - 1]:
                    valid = False
                    break
            for i in reversed(range(breakindex, length)):
                if arr[i] > arr[i - 1] or arr[i] == arr[i - 1]:
                    valid = False
        else:
            valid = False
        return valid
MySolution = Solution()
print(MySolution.validMountainArray([2,1]))
print(MySolution.validMountainArray([3,5,5]))
print(MySolution.validMountainArray([0,3,2,1]))
print(MySolution.validMountainArray([0,1,2,3,4,5,6,7,8,9]))
print(MySolution.validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]))
"""
Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true

[0,1,2,3,4,5,6,7,8,9]
false

[14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
false
 

Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 104Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true

[0,1,2,3,4,5,6,7,8,9]
false

[14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3]
false
 

Constraints:

    1 <= arr.length <= 104
    0 <= arr[i] <= 104"""