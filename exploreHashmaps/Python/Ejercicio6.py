class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sq_sum = 0
            while n > 0:
                sq_sum += (n%10)**2
                n = n//10
            n = sq_sum
        return True
sol = Solution()
#print(sol.isHappy(19))
print(sol.isHappy(20))
print(sol.isHappy(68))
#print(sol.isHappy(100))
            
            