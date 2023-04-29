from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return head
        #invert the first half of the list
        prev, current, fast = head, head.next, head.next
        while fast or fast.next:
            if not fast.next or not fast.next.next: 
                """
                this assignment must happen when the fast pointer
                reach the end of the list
                """
                first_half_head = prev
                # if it is even we stay
                if not fast.next:
                    second_half_head = current
                # else if the list is odd, we go ahead the middle node
                elif not fast.next.next:
                    second_half_head = current.next
                break
            fast = fast.next.next
            # here we are reversing the first half of the list
            head.next = current.next
            current.next = prev
            prev = current
            current = head.next
        # this breaks the first half of the list with the second part
        head.next = None
        #then we compare
        current_first = first_half_head
        current_second = second_half_head
        while current_first:
            if current_first.val != current_second.val:
                return False
            current_first = current_first.next
            current_second = current_second.next
        

        #current1 = first_half_head
        #current2 = second_half_head
        #while current1:
        #    print("firstLL", current1.val)
        #    print("secondtLL", current2.val)
            #if current1.next:
        #    current1 = current1.next
            #current2.next:
        #    current2 = current2.next

        return True 

node0 = ListNode(1)
node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(4)
node4 = ListNode(5)
node5 = ListNode(4)
node6 = ListNode(3)
node7 = ListNode(2)
node8 = ListNode(1)
node0.next = node1
node1.next = node2
#node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

sol = Solution()
print(sol.isPalindrome(node0))