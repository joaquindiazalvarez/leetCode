from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 0
        while i < len(arr):
            max = -1
            cont = 0
            if i < len(arr) - 2:
                for j in range(i+1,len(arr)):
                    if arr[max] < arr[j]:
                        max = j
            elif i == len(arr) - 2:
                max = len(arr) - 1
            else:
                arr[len(arr)-1] = -1
                break
            for k in range(i,max):
                arr[k] = arr[max]
                cont += 1
            i = max           
        return arr
mySolution = Solution()
print(mySolution.replaceElements([17,18,5,4,6,1]))
#Input: arr = [17,18,5,4,6,1]
#Output: [18,6,6,6,1,-1]