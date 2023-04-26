# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd = head
        even = head.next
        evenhead = even
        while odd and even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            even = even.next
            odd = odd.next
        odd.next = evenhead
        #current = head
        #while current:
        #    print(current.val)
        #    current = current.next
        return head

        
node0 = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(7)
node7 = ListNode(8)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
#node4.next = node5
node5.next = node6
node6.next = node7


sol = Solution()
print(sol.oddEvenList(node0))