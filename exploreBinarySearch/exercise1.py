from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            offset = (right - left)//2
            pivot = left + offset
            if nums[pivot] == target:
                return pivot
            if nums[pivot] < target:
                left += offset + 1
            elif nums[pivot] > target:
                right -= offset + 1
        return -1
sol = Solution()
print(sol.search([-1,0,3,5,9,12], 12))