class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=i
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res.append(i)
        return res