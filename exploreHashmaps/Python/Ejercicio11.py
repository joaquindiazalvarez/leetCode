from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = []
        for number in nums1:
            if number in seen:
                seen[number] += 1
            else:
                seen[number] = 1
        for number in nums2:
            if number in seen:
                seen[number] -= 1
                res.append(number)
                if seen[number] == 0:
                    del seen[number]

        return res