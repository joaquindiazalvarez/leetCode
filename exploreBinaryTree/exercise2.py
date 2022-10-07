from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.__dfs(root, [])
    def __dfs(self, root, list):
        if root == None:
            return list
        list = self.__dfs(root.left, list)
        list.append(root.val)
        return self.__dfs(root.right, list)