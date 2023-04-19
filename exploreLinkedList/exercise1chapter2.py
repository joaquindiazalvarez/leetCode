from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head.next
        while fast != None:
            if slow.val == fast.val and slow.next == fast.next:
                return True
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                fast = fast.next
        return False

sol = Solution()

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
#node4.next = node2

print(sol.hasCycle(node1))