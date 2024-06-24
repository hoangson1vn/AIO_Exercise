class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = list()

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Overflow")
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Underflow")
        self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue Empty")
        return self.__queue[0]
