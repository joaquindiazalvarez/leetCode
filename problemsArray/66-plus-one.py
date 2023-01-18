from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        index = len(digits) - 1          
        while carry == True:
            #two cases
            #1: the number only adds 1
            #2: the number carries a sum to next number
            #3: the number carries a sum to the most significative number
            if digits[index] < 9:
                carry = False
                digits[index] +=1
            elif index != 0 and digits[index] == 9:
                digits[index] = 0
            elif index == 0 and digits[index] == 9:
                digits[index] = 0
                digits.insert(0, 1)
                carry = False
            index -= 1
        return digits
sol = Solution()
#print(sol.plusOne([1,2,3]))
#print(sol.plusOne([4,3,2,1]))
print(sol.plusOne([9]))