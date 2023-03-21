class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace_map = {}
        for i in range(len(s)):
            if s[i] in replace_map and replace_map[s[i]] != t[i]:
                return False
            replace_map[s[i]] = t[i]
        return True, replace_map
    
sol = Solution()
print(sol.isIsomorphic("paper", "title"))
print(sol.isIsomorphic("foo", "bar"))
print(sol.isIsomorphic("egg", "add"))
print(sol.isIsomorphic("baba", "badc"))
