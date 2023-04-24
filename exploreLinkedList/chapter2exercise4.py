from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this if may be removed
        #if head.next == None:
        #    return None
        current = head
        # we give an ofset to the first pinter
        for i in range(n):
            current = current.next
            if current == None:
                head = head.next
                return head
        target_prev = head
        while current.next:
            current = current.next
            target_prev = target_prev.next
        target_prev.next = target_prev.next.next
        print(target_prev.val)
        return head
            
sol = Solution()

node0 = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

node5 = ListNode(1)
node6 = ListNode(2)
node5.next = node6

print(sol.removeNthFromEnd(node0, 2))