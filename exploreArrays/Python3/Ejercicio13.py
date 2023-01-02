class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        helper = []
        pointer = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[pointer] = nums[i]
                pointer += 1
            if nums[i] % 2 == 1:
                helper.append(nums[i])
        for i in range(len(helper)):
            nums[pointer + i] = helper[i]
        return nums        
sol = Solution()
print(sol.sortArrayByParity([1,2,3,4,5,6]))