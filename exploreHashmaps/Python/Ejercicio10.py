class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        actualFirst = -1
        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
        for i in range(len(s)):
            if seen[s[i]] == 1:
                return i
        return -1

sol = Solution()
print(sol.firstUniqChar("leetcode"))
        