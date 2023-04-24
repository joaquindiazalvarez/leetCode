# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.__rec(None, head, None)    
    def __rec(self, prev, current, head):
        if current == None:
            return head
        if current.next == None:
            head = current
        head = self.__rec(current, current.next, head)
        current.next = prev
        return head
    


node0 = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

node6 = ListNode(1)
node7 = ListNode(2)
node6.next = node7

sol = Solution()
print(sol.reverseList(node0))