# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
""" class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        while currA:
            while currB:
                if currA == currB:
                    return currA
                currB = currB.next
            currB = headB
            currA = currA.next
        return """
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        currA = headA
        while currA:
            seen.add(currA)
            currA = currA.next
        currB = headB
        while currB:
            if currB in seen:
                return currB
            currB = currB.next

        return seen

sol = Solution()

cnode1 = ListNode(8)
cnode2 = ListNode(4)
cnode3 = ListNode(5)
cnode1.next = cnode2
cnode2.next = cnode3

anode1 = ListNode(4)
anode2 = ListNode(1)
#anode3 = ListNode(8)
#anode4 = ListNode(4)
#anode5 = ListNode(5)
anode1.next = anode2
anode2.next = cnode1
#anode3.next = anode4
#anode4.next = anode5

bnode1 = ListNode(5)
bnode2 = ListNode(6)
bnode3 = ListNode(1)
#bnode4 = ListNode(8)
#bnode5 = ListNode(4)
#bnode6 = ListNode(5)
bnode1.next = bnode2
bnode2.next = bnode3
bnode3.next = cnode1
#bnode4.next = bnode5
#bnode5.next = bnode6



print(sol.getIntersectionNode(anode1, bnode1))