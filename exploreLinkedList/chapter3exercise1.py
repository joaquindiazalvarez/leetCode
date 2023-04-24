# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        slow, fast = head, head.next
        
        while fast:
            if fast.next == None:
                new_head = fast
            head.next = fast.next
            fast.next = slow
            slow = fast
            fast = head.next
        #fast = new_head
        #while fast:
        #    print (fast.val)
        #    fast = fast.next
        return new_head
    
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
print(sol.reverseList(node6))