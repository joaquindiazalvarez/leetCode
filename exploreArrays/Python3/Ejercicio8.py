from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        exist = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] == 2 * arr[i] and i != j:
                    exist = True
        return exist    
MySolution = Solution()
print(MySolution.checkIfExist([10,2,5,3]))
print(MySolution.checkIfExist([7,1,14,11]))
print(MySolution.checkIfExist([3,1,7,11]))


"""
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

 

Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3
"""        