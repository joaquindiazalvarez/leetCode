class MyLinkedList:
    class ListNode:
        def __init__(self, val):
            self.prev = None
            self.next = None
            self.val = val
    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        current = self.head
        for _ in range(index):
            if current:
                current = current.next
            else:
                return
        return current.val

    def addAtHead(self, val: int) -> None:
        new = self.ListNode(val)
        if self.head:
            new.next = self.head
            self.head.prev = new
        self.head = new
        return new

    def addAtTail(self, val: int) -> None:
        new = self.ListNode(val)
        if not self.head:
            self.addAtHead(val)
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new
        new.prev = current
        return new

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        new = self.ListNode(val)
        current = self.head
        for _ in range(index):
            if current.next:
                current = current.next
            else:
                self.addAtTail(val)
                return new
        new.prev = current.prev
        new.next = current
        new.prev.next = new
        current.prev = new
        return new

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current = self.head
        for _ in range(index):
            if current.next:
                current = current.next
            else:
                return
        current.prev.next = current.next
        current.next.prev = current.prev
        return current


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

#["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
#[[], [1], [3], [1, 2], [1], [1], [1]]
obj = MyLinkedList()
print(obj.addAtIndex(0,10))
print(obj.addAtIndex(0,20))
print(obj.addAtIndex(1,30))
print(obj.get(1))
"""
print(obj.addAtHead(1))
print(obj.addAtTail(3))
print(obj.addAtIndex(1,2))
print(obj.deleteAtIndex(1))
print(obj.get(1))
"""