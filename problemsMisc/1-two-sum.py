from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] + nums[i] == target and i!=j:
                    return [i, j]
"""
            searched = self.binary_search(nums, sum_target, i)
            if searched != -1:
                return [i, searched]
"""
"""    def binary_search(self, array, target, selfindex):
            left = 0
            right = len(array) - 1
            while left <= right:
                pivot = left + (right - left)//2
                if array[pivot] == target:
                    if pivot == selfindex:
                        return -1
                    return pivot
                if target < array[pivot]:
                    right = pivot - 1
                elif target > array[pivot]:
                    left = pivot + 1
                if left > right and array[pivot] != target:
                    return -1
"""

sol = Solution()
#print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))