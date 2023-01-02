class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer] = nums[i]
                pointer += 1
            if nums[i] == 0:
                zeros += 1
        for i in range(1, zeros + 1):
            nums[-i] = 0
        return pointer, nums
sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))