from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.__dfs(p, q, True)
    def __dfs(self, node1, node2, same):
        if node1 and node2:
            if node1.val != node2.val:
                same = False
        if (node1 and not node2) or (not node1 and node2):
                same = False
        if node1 == None or node2 == None:
            return same
        same = self.__dfs(node1.left, node2.left, same)
        return self.__dfs(node1.right, node2.right, same)

"""         first = self.__dfs(p, [])
        second = self.__dfs(q, [])
        return first == second
    def __dfs(self, node, list):
        if node == None:
            return list
        list = self.__dfs(node.left, list)
        list.append(node.val)
        return self.__dfs(node.right, list)
    def test(self, node):
        return self.__dfs(node, []) """

ultimo1 = TreeNode(3)
ultimo2 = TreeNode(4)
penultimo = TreeNode(2, ultimo1, ultimo2)
antepenultimo = TreeNode(1, penultimo)

ult1 = TreeNode(3)
ult2 = TreeNode(5)
pen = TreeNode (2, ult1, ult2)
ant = TreeNode(1, pen, pen)

sol = Solution()
print(sol.isSameTree(antepenultimo, ant))