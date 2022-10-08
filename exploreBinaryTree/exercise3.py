from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.__dfs(root, [])
    def __dfs(self, root, list):
        if root == None:
            return list
        list = self.__dfs(root.left, list)
        #if root.left != None:
        #    list.append(root.val)
        list = self.__dfs(root.right, list)
        list.append(root.val)
        #return self.__dfs(root.right, list)
        return list

tercer = TreeNode(3)
segundo = TreeNode(2, tercer)
primer = TreeNode(1, None, segundo)
sol = Solution()
print(sol.postorderTraversal(primer))