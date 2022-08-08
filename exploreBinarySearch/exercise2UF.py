class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        possibleSquareRoots = []
        for i in range(1, (x//2) + 1):
            possibleSquareRoots.append(i)
        return possibleSquareRoots
        target = x
        left = 0
        right = len(possibleSquareRoots) - 1
        while left <= right:
            pivot = left + (right - left)//2
            squareRoot = possibleSquareRoots[pivot]
            if squareRoot ** 2 == target:
                return squareRoot
            if squareRoot ** 2 < target:
                left = pivot + 1
            elif squareRoot ** 2 > target:
                right = pivot - 1
            #if left == right and left == pivot:
             #   return square
            if left > right: 
                if squareRoot ** 2 < target:
                    return squareRoot
                else:
                    return possibleSquareRoots[pivot - 1]

        return squareRoot
        #funciona pero con numeros grandes se demora mucho
sol = Solution()
print(sol.mySqrt())
#print(sol.mySqrt(6))
#print(sol.mySqrt(35))
#print(sol.mySqrt(48))