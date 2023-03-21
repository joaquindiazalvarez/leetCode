from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set()
        seen2 = set()
        for element in nums1:
            seen1.add(element)
        for element in nums2:
            seen2.add(element)
        return list(seen1.intersection(seen2))
# Can be improved using just one set, then iterate the second array, 
# and if the element is in the first set, append to res, and delete from first set
sol = Solution()
print(sol.intersection([1,2,2,1], [2,2]))
print(sol.intersection([4,9,5], [9,4,9,8,4]))