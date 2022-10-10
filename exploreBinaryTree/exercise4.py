from sys import _current_frames
from typing import Optional, List
# Definition for a binary tree node.
class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    head = Node(None)
    tail = Node(None)
    def isEmpty(self):
        return self.head != None
    def peek(self):
        return self.head.data
    def enqueue(self, data):
        new = self.Node(data)
        if self.head.data == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        return new
    def dequeue(self):
        deq = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return deq
    def __str__(self):
        current = self.head
        str_con = ""
        while current != None:
            str_con += f'[{current.data}],'
            current = current.next
        return str_con

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = Queue()
        arr1 = []
        arr1.append([root.val])
        queue.enqueue(root.val)
        current = queue.head
        while current != None:
            arr2 = []
            prev = root
            if root.left != None:
                root = root.left
            #if not(root.right == None and root.left == None and prev.right == None):
                queue.enqueue(root.val)
                arr2.append(root.val)
            #if root.left != None:
            #    queue.enqueue(root.left.val)
            if prev.right != None:
                root = prev.right
            #if not(root.right == None and root.left == None and prev.right == None):
                queue.enqueue(root.val)
                arr2.append(root.val)
            if not(prev.left == None and prev.right == None):
                arr1.append(arr2)
            if prev.left != None:
                root = prev.left
            current = current.next
        print(queue)
        return(arr1)


#queue = Queue()
#queue.enqueue(1)
#queue.enqueue(2)
#queue.enqueue(3)
#queue.dequeue()
#print(queue)          
ultimo1 = TreeNode(15)
ultimo2 = TreeNode(7)
penultimo1 = TreeNode(9)
penultimo2 = TreeNode(20, ultimo1, ultimo2)
antepenultimo = TreeNode(3, penultimo1, penultimo2)
#ultimo = TreeNode(2)
#penultimo = TreeNode(1, ultimo)
#ultimoleft = TreeNode(4)
#ultimoright = TreeNode(5)
#penultimoleft = TreeNode(2, ultimoleft, ultimoright)
#penultimoright = TreeNode(3)
#antepenultimo = TreeNode(1, penultimoleft, penultimoright)
sol = Solution()
print(sol.levelOrder(antepenultimo))
