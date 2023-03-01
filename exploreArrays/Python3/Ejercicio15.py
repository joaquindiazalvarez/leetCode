from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected =  heights[:]
        wrong = 0
        for i in range(len(expected)):
            current = i
            while expected[current] < expected[current - 1] and current >= 1:
                changed = expected[current]
                expected[current] = expected[current - 1]
                expected[current - 1] = changed
                current -= 1
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                wrong += 1
        return  wrong
sol = Solution()
print(sol.heightChecker([5,1,2,3,4]))