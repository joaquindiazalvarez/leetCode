class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        left = 2
        right = x//2 
        target = x
        while left <= right:
            pivot = left + (right - left)//2
            power = pivot * pivot
            #if power == target:
            #    return squareRoot
            if power < target:
                left = pivot + 1
            elif power > target:
                right = pivot - 1
            #if left == right and left == pivot:
             #   return square
            #if left > right: 
              #  if squareRoot ** 2 < target:
               #     return squareRoot
                #else:
                 #   return possibleSquareRoots[pivot - 1]
            else:
                return pivot
        return right
sol = Solution()
print(sol.mySqrt(225))
#print(sol.mySqrt(6))
#print(sol.mySqrt(35))
#print(sol.mySqrt(48))