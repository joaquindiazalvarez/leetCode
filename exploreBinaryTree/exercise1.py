from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.__dfs(root, [])
    def __dfs(self, root, list):
        if root == None:
            return list
        list.append(root.val)
        list = self.__dfs(root.left, list)
        return self.__dfs(root.right, list)

tercer = TreeNode(3)
segundo = TreeNode(2, tercer)
primer = TreeNode(1, None, segundo)
sol = Solution()
print(sol.preorderTraversal(primer))