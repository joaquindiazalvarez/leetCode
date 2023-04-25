# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        currentprint = dummy.next
        while currentprint:
            print(currentprint.val)
            currentprint = currentprint.next
        return dummy.next
node0 = ListNode(7)
node1 = ListNode(7)
node2 = ListNode(7)
node3 = ListNode(7)
node4 = ListNode(7)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

sol = Solution()
print(sol.removeElements(node0, 7))