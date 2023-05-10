import collections
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
ultimo4 = TreeNode(3)
ultimo3 = TreeNode(5)
ultimo2 = TreeNode(7)
ultimo1 = TreeNode(15)
penultimo2 = TreeNode(2, ultimo3, ultimo4)
penultimo1 = TreeNode(9, ultimo1, ultimo2)
antepenultimo = TreeNode(1, penultimo1, penultimo2)
sol = Solution()
print(sol.hasPathSum(antepenultimo, 25))