from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appearances = {1:set(), 2:set()}
        for element in nums:
            if element in appearances[1]:
                appearances[2].add(element)
                appearances[1].discard(element)
            else:
                appearances[1].add(element)
        return list(appearances[1])[0]
#It can be improved by having just 1 set, and when the next element is already
#in the set, remove it, so we only got the single number at the end.
#Another solution is with bit manipulation
sol = Solution()
print(sol.singleNumber([2,2,1]))
print(sol.singleNumber([4,1,2,1,2]))
print(sol.singleNumber([1]))