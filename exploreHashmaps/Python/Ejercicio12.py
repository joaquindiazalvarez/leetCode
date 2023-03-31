from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                condition = abs(seen[nums[i]] - i) <= k
                if condition:
                    return True
                else:
                    seen[nums[i]] = i
            else:
                seen[nums[i]] = i
        return False