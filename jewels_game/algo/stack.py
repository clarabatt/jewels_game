class Stack:
    def __init__(self, cap=10):
        self.stack = [None] * cap
        self.cap = cap
        self.size = 0

    def capacity(self):
        return self.cap

    def push(self, data):
        if self.size >= self.cap:
            self.cap = self.cap * 2
            newStack = [None] * self.cap
            for i in range(self.size):
                newStack[i] = self.stack[i]
            self.stack = newStack
        self.stack[self.size] = data
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop() used on empty stack")
        poppedVal = self.stack[self.size - 1]
        self.stack[self.size - 1] = None
        self.size -= 1
        return poppedVal

    def get_top(self):
        if self.is_empty():
            return None
        return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size
