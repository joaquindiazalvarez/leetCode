class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        seen = {}
        minimum = 2001
        common = ''
        for i in range(len(list1)):
            seen[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in seen:
                prevIndex = seen[list2[j]]
                if prevIndex + j < minimum:
                    minimum = prevIndex + j
                    common = [list2[j]]
                elif prevIndex + j == minimum:
                    common.append(list2[j])
        return common