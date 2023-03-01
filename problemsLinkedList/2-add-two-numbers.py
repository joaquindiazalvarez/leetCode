from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        carry = 0
        add = l1.val + l2.val
        if add > 9:
            newval = add - 10
            carry = 1
        else:
            newval = add
        result_head = ListNode(newval)
        current1 = l1.next
        current2 = l2.next
        prev3 = result_head
        add = 0
        while current1 or current2:
            if current1:
                add += current1.val
            if current2:
                add += current2.val
            add += carry
            carry = 0
            if add > 9:
                newval = add - 10
                carry = 1
            else:
                newval = add
            add = 0    
            current3 = ListNode(newval)
            prev3.next = current3
            prev3 = current3
            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next
        if carry == 1:
            current3 = ListNode(1)
            prev3.next = current3
        current = result_head
        while current:
            print(current.val)
            current = current.next
        return result_head

linked1_7 = ListNode(9)
linked1_6 = ListNode(9, linked1_7)
linked1_5 = ListNode(9, linked1_6)
linked1_4 = ListNode(9, linked1_5)
linked1_3 = ListNode(9, linked1_4)
linked1_2 = ListNode(9, linked1_3)
linked1_1 = ListNode(9, linked1_2)

linked2_4 = ListNode(9)
linked2_3 = ListNode(9, linked2_4)
linked2_2 = ListNode(9, linked2_3)
linked2_1 = ListNode(9, linked2_2)
sol = Solution()
sol.addTwoNumbers(linked1_1, linked2_1)

