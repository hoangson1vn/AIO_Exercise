class Stack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = list()

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, value):
        if self.is_full():
            raise OverflowError("Overflow")
        self.__stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Underflow")
        self.__stack.pop(-1)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack Empty")
        return self.__stack[-1]
