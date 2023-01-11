class MyCircularQueue:

    def __init__(self, k: int):
        self.__queue_size = k
        self.__queue = []
        self.__head = 0
        self.__tail = 0
        for i in range(k):
            self.__queue.append(None)

    def enQueue(self, value: int) -> bool:
        #adds one element to the tail
        #tail index += 1
        #then queue at tail index = value
        if self.isEmpty():
            self.__queue[0] = value
            self.__head = 0
            self.__tail = 0
            return True
        else:
            if not self.isFull():
                self.__tail += 1
                if self.__tail >= self.__queue_size:
                    self.__tail = 0
                self.__queue[self.__tail] = value
                return True
            else:
                return False


    def deQueue(self) -> bool:
        #delete element from the head
        #queue at head index = None
        #head index += 1
        if self.isEmpty():
            return False
        else:
            self.__queue[self.__head] = None
            if self.__head == self.__queue_size - 1:
                self.__head = 0
            else: 
                self.__head += 1
            return True        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.__queue[self.__head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.__queue[self.__tail]

    def isEmpty(self) -> bool:
        return self.__queue[self.__head] == None or self.__queue[self.__tail] == None
            
    def isFull(self) -> bool:
        if self.isEmpty():
            return False
        return self.__tail == (self.__head - 1) or (self.__head == 0 and self.__tail == (self.__queue_size - 1))    


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear(), "rear")
print(obj.isFull(), "isFull")
obj.deQueue()
print(obj.enQueue(4))
print(obj.Rear(), "rear")

"""
print(obj.Front(), "front")
print(obj.Rear(), "rear")
print(obj.isEmpty(), "isEmpty")
print(obj.isFull(), "isFull")
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
obj.enQueue(5)
obj.enQueue(6)
obj.enQueue(7)
print("added 1, 2 and 3, 4, 5, 6, 7 to the queue")
print(obj.Front(), "front")
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
print(obj.isEmpty(), "isEmpty")
print(obj.isFull(), "isFull")
obj.deQueue()
print(obj.Front(), "front")
print(obj.Rear(), "rear")
print(obj.isEmpty(), "isEmpty")
print(obj.isFull(), "isFull")
obj.deQueue()
obj.deQueue()
obj.deQueue()
print(obj.Front(), "front")
print(obj.Rear(), "rear")
print(obj.isEmpty(), "isEmpty")
print(obj.isFull(), "isFull")
obj.deQueue()
print(obj.Front(), "front")
print(obj.Rear(), "rear")
print(obj.isEmpty(), "isEmpty")
print(obj.isFull(), "isFull")

# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
"""