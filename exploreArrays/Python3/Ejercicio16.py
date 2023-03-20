from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minimum = -2**32 - 1
        maximums = {1: minimum, 2: minimum, 3: minimum }
        for element in nums:
            for i in reversed(range(1,4)):
                if i > 1 and element == maximums[i - 1] or element == maximums[1]:
                    break
                if element > maximums[i]:
                    if i < 3:
                        maximums[i + 1] = maximums[i] 
                        maximums[i] = element
                    else:
                        maximums[i] = element
        if maximums[3] < minimum + 1:
            return maximums[1]
        else:
            return maximums[3]
            

sol = Solution()
#print(sol.thirdMax([3,2,1]))
print(sol.thirdMax([1,2,2]))
#print(sol.thirdMax([2,2,3,1]))