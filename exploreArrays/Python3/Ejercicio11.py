class Solution(object):
    def removeDuplicates(self, nums):
        j = 1
        for i in range(len(nums)- 1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j += 1
        return j, nums
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,2,2,2,2,2,2,2,2,3,3,4,4]))