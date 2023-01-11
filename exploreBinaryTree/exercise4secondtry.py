from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res



ultimo1 = TreeNode(15)
ultimo2 = TreeNode(7)
ultimo3 = TreeNode(5)
ultimo4 = TreeNode(3)
penultimo1 = TreeNode(9, ultimo3, ultimo4)
penultimo2 = TreeNode(20, ultimo1, ultimo2)
antepenultimo = TreeNode(3, penultimo1, penultimo2)
sol = Solution()
print(sol.levelOrder(antepenultimo))