from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.__dfs(root, root, True)
    def __dfs(self, node1, node2, isSymmetric):
        if node1 == None and node2 == None:
            return isSymmetric
        if node1 and node2:
            if node1.val != node2.val:
                return False
        elif (node1 and node2 == None) or (node1 == None and node2):
            return False
        isSymmetric = self.__dfs(node1.left, node2.right, isSymmetric)
        return self.__dfs(node1.right, node2.left, isSymmetric)

uno_ultimo1 = TreeNode(7)
#uno_ultimo2 = TreeNode(6)
uno_ultimo3 = TreeNode(7)
#uno_ultimo4 = TreeNode(7)
uno_penultimo1 = TreeNode(3, uno_ultimo1, None)
uno_penultimo2 = TreeNode(3, uno_ultimo3, None)
uno_antepenultimo = TreeNode(1, uno_penultimo1, uno_penultimo2)
sol = Solution()
print(sol.isSymmetric(uno_antepenultimo))

uno_last = TreeNode()
uno_last = TreeNode()
uno_last = TreeNode()
uno_last = TreeNode()
uno_last = TreeNode()
uno_last = TreeNode()
uno_last = TreeNode()