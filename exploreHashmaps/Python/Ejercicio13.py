from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
    
        for s in strs:
            key = "".join(sorted(list(s)))
            lookup[key.append(s)]
        output = []
        for l in lookup.values():
            output.append(l)
        return output