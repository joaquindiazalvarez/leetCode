# Definition for a binary tree node.
from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = -1
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
            res += 1
        return res
    

#ultimo1 = TreeNode(15)
#ultimo2 = TreeNode(7)
#ultimo3 = TreeNode(5)
#ultimo4 = TreeNode(3)
#penultimo1 = TreeNode(9, ultimo3, ultimo4)
penultimo2 = TreeNode(2)
antepenultimo = TreeNode(1, penultimo2)
sol = Solution()
print(sol.maxDepth(antepenultimo))