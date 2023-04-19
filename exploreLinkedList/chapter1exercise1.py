class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        current = self.head
        actualIndex = 0
        while actualIndex != index and current != None:
            current = current.next
            actualIndex += 1
        if current != None:
            return current.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head = new

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.addAtHead(val)
            return
        new = Node(val)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        if index == 0:
            self.addAtHead(val)
            return
        actualIndex = 1
        #we apply an offset of 1 to obtain prev instead of node at index
        current = self.head
        while actualIndex != index and current != None:
            current = current.next
            actualIndex += 1
        if current == None:
            return -1
        prev = current
        following = current.next
        prev.next = new
        new.next = following


    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        actualIndex = 1
        #we give an offset to obtain previous node
        current = self.head
        while actualIndex != index and current != None:
            current = current.next
            actualIndex += 1
        if current == None or current.next == None:
            return -1
        prev = current
        following = current.next.next
        prev.next = following

""" linked = MyLinkedList()
print(linked.addAtHead(7))
print(linked.addAtHead(2))
print(linked.addAtHead(1))
print(linked.addAtIndex(3, 0))
print(linked.deleteAtIndex(2))
print(linked.addAtHead(6))
print(linked.addAtTail(4))
print(linked.get(4))
print(linked.addAtHead(4))
print(linked.addAtIndex(5, 0))
print(linked.addAtHead(6)) """



#Input: ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
#[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
#Output: [null,null,null,null,null,null,null,null,-1,null,null,null]
#Expected: [null,null,null,null,null,null,null,null,4,null,null,null]

linked = MyLinkedList()
print(linked.addAtIndex(0, 10))
print(linked.addAtIndex(0, 20))
print(linked.addAtIndex(1, 30))
print(linked.get(0))

#Input: ["MyLinkedList","addAtIndex","addAtIndex","addAtIndex","get"]
#[[],[0,10],[0,20],[1,30],[0]]
#Output: [null,null,null,null,-1]
#Expected: [null,null,null,null,20]

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)